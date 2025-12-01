"""
Claude Agent Router Service
FastAPI service that routes agent requests to Claude API or Groq API
Deployed on Google Cloud Run at port 8083
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from anthropic import Anthropic
import os
import yaml
import httpx
from typing import Dict, List, Any
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Claude Agent Router",
    description="Routes agent requests to appropriate LLM providers",
    version="1.0.0"
)

# Initialize clients
claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
groq_api_url = os.getenv("GROQ_API_URL", "http://groq-inference-proxy:8082")

# Agent config cache
agent_configs: Dict[str, Dict] = {}


def load_agent_config(agent_id: str) -> Dict[str, Any]:
    """Load agent configuration from YAML file"""
    if agent_id in agent_configs:
        return agent_configs[agent_id]

    # Try to find config file
    config_paths = [
        Path(f"/app/configs/{agent_id}.yaml"),
        Path(f"/app/configs/instances/{agent_id}.yaml"),
    ]

    for config_path in config_paths:
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                agent_configs[agent_id] = config
                logger.info(f"Loaded config for agent {agent_id}")
                return config

    raise HTTPException(
        status_code=404,
        detail=f"Agent configuration not found for {agent_id}"
    )


def build_claude_messages(request_data: Dict) -> List[Dict]:
    """Convert request to Claude messages format"""
    messages = request_data.get("messages", [])

    # Ensure proper format
    formatted_messages = []
    for msg in messages:
        if isinstance(msg, dict) and "role" in msg and "content" in msg:
            formatted_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

    return formatted_messages


def extract_tool_definitions(config: Dict) -> List[Dict]:
    """Extract tool definitions from agent config for Claude function calling"""
    tools = config.get("agent", {}).get("tools", [])

    claude_tools = []
    for tool in tools:
        claude_tool = {
            "name": tool["name"],
            "description": tool["description"],
            "input_schema": {
                "type": "object",
                "properties": tool.get("parameters", {}),
                "required": [
                    param_name
                    for param_name, param_def in tool.get("parameters", {}).items()
                    if param_def.get("required", False)
                ]
            }
        }
        claude_tools.append(claude_tool)

    return claude_tools


@app.get("/health")
async def health_check():
    """Health check endpoint for Cloud Run"""
    return {
        "status": "healthy",
        "service": "claude-agent-router",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/v1/agents")
async def list_agents():
    """List all configured agents"""
    configs_dir = Path("/app/configs/instances")

    if not configs_dir.exists():
        return {"agents": []}

    agents = []
    for config_file in configs_dir.glob("*.yaml"):
        try:
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                agent_info = config.get("agent", {})
                agents.append({
                    "id": agent_info.get("id"),
                    "name": agent_info.get("name"),
                    "type": agent_info.get("type"),
                    "vertical": agent_info.get("vertical"),
                    "model": agent_info.get("model", {}).get("name")
                })
        except Exception as e:
            logger.error(f"Error loading {config_file}: {e}")

    return {"agents": agents}


@app.post("/v1/agents/{agent_id}/invoke")
async def invoke_agent(agent_id: str, request: Request):
    """
    Invoke an agent with a request

    Request body:
    {
        "messages": [
            {"role": "user", "content": "Analyze customer health for customer_123"}
        ],
        "tool_choice": "auto" (optional),
        "max_tokens": 4000 (optional)
    }
    """
    try:
        request_data = await request.json()

        # Load agent configuration
        config = load_agent_config(agent_id)
        agent_config = config.get("agent", {})
        model_config = agent_config.get("model", {})

        provider = model_config.get("provider", "anthropic")

        # Route to appropriate provider
        if provider == "anthropic":
            return await invoke_claude(agent_config, request_data)
        elif provider == "groq":
            return await invoke_groq(agent_config, request_data)
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported provider: {provider}"
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error invoking agent {agent_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


async def invoke_claude(agent_config: Dict, request_data: Dict) -> JSONResponse:
    """Invoke Claude API"""
    model_config = agent_config.get("model", {})

    # Build messages
    messages = build_claude_messages(request_data)

    # Get system prompt
    system_prompt = agent_config.get("system_prompt", "")

    # Replace template variables (e.g., {VERTICAL})
    vertical = agent_config.get("vertical", "")
    system_prompt = system_prompt.replace("{VERTICAL}", vertical.title())

    # Extract tools for function calling
    tools = extract_tool_definitions({"agent": agent_config})

    # Prepare Claude API request
    claude_params = {
        "model": model_config.get("name", "claude-sonnet-4.5"),
        "max_tokens": request_data.get("max_tokens", model_config.get("max_tokens", 4000)),
        "temperature": model_config.get("temperature", 0.7),
        "system": system_prompt,
        "messages": messages
    }

    # Add tools if available
    if tools:
        claude_params["tools"] = tools
        claude_params["tool_choice"] = request_data.get("tool_choice", {"type": "auto"})

    try:
        # Call Claude API
        response = claude_client.messages.create(**claude_params)

        # Log usage for cost tracking
        usage = response.usage
        logger.info(
            f"Claude API call - Agent: {agent_config.get('id')} - "
            f"Input tokens: {usage.input_tokens} - "
            f"Output tokens: {usage.output_tokens}"
        )

        # Convert to dict
        response_dict = {
            "id": response.id,
            "type": response.type,
            "role": response.role,
            "content": [
                {
                    "type": block.type,
                    "text": block.text if hasattr(block, 'text') else None,
                    "id": getattr(block, 'id', None),
                    "name": getattr(block, 'name', None),
                    "input": getattr(block, 'input', None)
                }
                for block in response.content
            ],
            "model": response.model,
            "stop_reason": response.stop_reason,
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens
            }
        }

        return JSONResponse(content=response_dict)

    except Exception as e:
        logger.error(f"Claude API error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Claude API error: {str(e)}")


async def invoke_groq(agent_config: Dict, request_data: Dict) -> JSONResponse:
    """Route to Groq API via existing groq-inference-proxy service"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{groq_api_url}/v1/chat/completions",
                json={
                    "model": agent_config.get("model", {}).get("name", "llama-3.1-70b-versatile"),
                    "messages": request_data.get("messages", []),
                    "temperature": agent_config.get("model", {}).get("temperature", 0.7),
                    "max_tokens": request_data.get("max_tokens", 4000)
                },
                timeout=30.0
            )
            response.raise_for_status()
            return JSONResponse(content=response.json())

    except httpx.HTTPError as e:
        logger.error(f"Groq API error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")


@app.post("/v1/agents/{agent_id}/tools/execute")
async def execute_tool(agent_id: str, request: Request):
    """
    Execute a tool call from the agent

    Request body:
    {
        "tool_name": "query_crm",
        "tool_input": {"customer_id": "cust_123", "timeframe_days": 90}
    }
    """
    try:
        request_data = await request.json()
        tool_name = request_data.get("tool_name")
        tool_input = request_data.get("tool_input", {})

        # Load agent config to get tool definitions
        config = load_agent_config(agent_id)
        agent_config = config.get("agent", {})

        # Find tool definition
        tools = agent_config.get("tools", [])
        tool_def = next((t for t in tools if t["name"] == tool_name), None)

        if not tool_def:
            raise HTTPException(
                status_code=404,
                detail=f"Tool '{tool_name}' not found for agent {agent_id}"
            )

        # Execute tool based on endpoint or logic
        endpoint = tool_def.get("endpoint")

        if endpoint:
            # Make API call to external service
            async with httpx.AsyncClient() as client:
                # Replace path parameters
                final_endpoint = endpoint
                for key, value in tool_input.items():
                    final_endpoint = final_endpoint.replace(f"{{{key}}}", str(value))

                response = await client.get(final_endpoint)
                response.raise_for_status()
                return JSONResponse(content=response.json())
        else:
            # Execute internal logic (placeholder)
            return JSONResponse(content={
                "status": "success",
                "tool": tool_name,
                "result": "Tool executed (internal logic not yet implemented)"
            })

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error executing tool {tool_name}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8083)
