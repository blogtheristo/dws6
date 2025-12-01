"""
Groq Agent Router - MVP Version
Simplified FastAPI service for MVP pilot using Groq free tier
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import os
import yaml
import httpx
from typing import Dict, List, Any
import logging
from datetime import datetime
from pathlib import Path
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Groq Agent Router - MVP",
    description="Routes agent requests to Groq API (free tier)",
    version="1.0.0-mvp"
)

# Groq API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Agent config cache
agent_configs: Dict[str, Dict] = {}

# Cost tracking (for investor demo)
total_tokens_used = 0
total_cost_eur = 0.0


def load_agent_config(agent_id: str) -> Dict[str, Any]:
    """Load agent configuration from YAML file"""
    if agent_id in agent_configs:
        return agent_configs[agent_id]

    # Try to find config file
    config_paths = [
        Path(f"/app/configs/{agent_id}.yaml"),
        Path(f"/app/configs/mvp/{agent_id}.yaml"),
        Path(f"configs/mvp/{agent_id}.yaml"),  # For local dev
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


@app.get("/health")
async def health_check():
    """Health check endpoint for Cloud Run"""
    return {
        "status": "healthy",
        "service": "groq-agent-router-mvp",
        "timestamp": datetime.utcnow().isoformat(),
        "groq_api_configured": GROQ_API_KEY is not None
    }


@app.get("/v1/agents")
async def list_agents():
    """List all MVP agents"""
    return {
        "agents": [
            {
                "id": "customersat-construction-mvp",
                "name": "Customer Satisfaction Agent - MVP",
                "type": "customer_satisfaction",
                "vertical": "construction",
                "model": "groq/llama-3.1-70b-versatile"
            },
            {
                "id": "viability-construction-mvp",
                "name": "Viability Agent - MVP",
                "type": "viability",
                "vertical": "construction",
                "model": "groq/llama-3.1-70b-versatile"
            }
        ],
        "mvp_mode": True,
        "pilot_customers": 5
    }


@app.get("/v1/metrics")
async def get_metrics():
    """Get cost metrics for investor demo"""
    global total_tokens_used, total_cost_eur

    return {
        "total_invocations": len(agent_configs),
        "total_tokens_used": total_tokens_used,
        "estimated_cost_eur": total_cost_eur,
        "cost_per_token_eur": 0.0007 / 1000,  # Groq pricing
        "using_free_credits": True,
        "actual_cost_eur": 0.0  # Free with startup credits
    }


@app.post("/v1/agents/{agent_id}/invoke")
async def invoke_agent(agent_id: str, request: Request):
    """
    Invoke an agent via Groq API

    Request body:
    {
        "messages": [
            {"role": "user", "content": "Analyze customer health..."}
        ],
        "customer_data": {...}  (optional)
    }
    """
    global total_tokens_used, total_cost_eur

    try:
        request_data = await request.json()

        # Load agent configuration
        config = load_agent_config(agent_id)
        agent_config = config.get("agent", {})
        model_config = agent_config.get("model", {})

        # Get system prompt
        system_prompt = agent_config.get("system_prompt", "")

        # Build messages for Groq
        messages = [
            {"role": "system", "content": system_prompt}
        ]

        # Add user messages
        user_messages = request_data.get("messages", [])
        for msg in user_messages:
            messages.append({
                "role": msg.get("role", "user"),
                "content": msg.get("content", "")
            })

        # Add customer data if provided
        customer_data = request_data.get("customer_data")
        if customer_data:
            messages.append({
                "role": "user",
                "content": f"Customer Data (JSON): {json.dumps(customer_data)}"
            })

        # Prepare Groq API request
        groq_payload = {
            "model": model_config.get("name", "llama-3.1-70b-versatile"),
            "messages": messages,
            "temperature": model_config.get("temperature", 0.7),
            "max_tokens": model_config.get("max_tokens", 1500)
        }

        # Call Groq API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                GROQ_API_URL,
                json=groq_payload,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                timeout=30.0
            )

            response.raise_for_status()
            groq_response = response.json()

        # Track usage for cost metrics
        usage = groq_response.get("usage", {})
        tokens_used = usage.get("total_tokens", 0)
        total_tokens_used += tokens_used

        # Groq pricing: ~$0.70 per 1M tokens (but free with credits)
        cost_eur = (tokens_used / 1_000_000) * 0.70
        total_cost_eur += cost_eur

        # Log usage
        logger.info(
            f"Groq API call - Agent: {agent_id} - "
            f"Tokens: {tokens_used} - "
            f"Cost: €{cost_eur:.4f} (covered by free credits)"
        )

        # Return response
        return JSONResponse(content={
            "agent_id": agent_id,
            "response": groq_response.get("choices", [{}])[0].get("message", {}).get("content", ""),
            "model": groq_response.get("model"),
            "usage": usage,
            "cost_eur": 0.0,  # Free with credits
            "timestamp": datetime.utcnow().isoformat()
        })

    except httpx.HTTPStatusError as e:
        logger.error(f"Groq API error: {e.response.status_code} - {e.response.text}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Groq API error: {e.response.text}"
        )
    except Exception as e:
        logger.error(f"Error invoking agent {agent_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/v1/agents/{agent_id}/analyze-customer")
async def analyze_customer(agent_id: str, request: Request):
    """
    Convenience endpoint for customer analysis

    Request body:
    {
        "customer_id": "cust_001",
        "nps_score": 8,
        "open_tickets": 2,
        "days_since_contact": 15,
        "monthly_revenue_eur": 2000,
        "setup_hours": 8
    }
    """
    try:
        customer_data = await request.json()
        customer_id = customer_data.get("customer_id", "unknown")

        # Load agent config to determine analysis type
        config = load_agent_config(agent_id)
        agent_type = config.get("agent", {}).get("type")

        if agent_type == "customer_satisfaction":
            prompt = f"""
            Analyze this customer's health:

            Customer ID: {customer_id}
            NPS Score: {customer_data.get('nps_score', 'N/A')}
            Open Support Tickets: {customer_data.get('open_tickets', 'N/A')}
            Days Since Last Contact: {customer_data.get('days_since_contact', 'N/A')}
            Equipment Usage Trend: {customer_data.get('usage_trend', 'Stable')}

            Provide analysis in JSON format as specified in your system prompt.
            """

        elif agent_type == "viability":
            prompt = f"""
            Calculate viability metrics for this customer:

            Customer ID: {customer_id}
            Setup Hours: {customer_data.get('setup_hours', 'N/A')}
            Monthly Revenue: €{customer_data.get('monthly_revenue_eur', 'N/A')}

            Use the constants and formulas from your system prompt.
            Provide calculation in JSON format.
            """

        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown agent type: {agent_type}"
            )

        # Call invoke endpoint
        return await invoke_agent(
            agent_id=agent_id,
            request=Request(
                scope={
                    "type": "http",
                    "method": "POST",
                    "headers": []
                },
                receive=lambda: {"body": json.dumps({
                    "messages": [{"role": "user", "content": prompt}]
                }).encode()}
            )
        )

    except Exception as e:
        logger.error(f"Error analyzing customer: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8083)
