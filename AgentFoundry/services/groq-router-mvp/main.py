"""
DWS IQ Agent Router - MVP
FastAPI service with 2 AI agents using Groq API

Agents:
1. Customer Satisfaction Agent - Analyzes customer health and churn risk
2. Viability Agent - Calculates payback period and unit economics

Cost: €0 (using Groq credits)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import httpx
import os
from datetime import datetime
from typing import Optional, Dict, Any
import json

app = FastAPI(
    title="DWS IQ Agent Router - MVP",
    version="1.0.0",
    description="AI agents for construction industry customer analysis"
)

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dws10.com",
        "https://www.dws10.com",
        "https://onelifetime.world",
        "https://www.onelifetime.world",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")

# Request/Response Models
class CustomerHealthRequest(BaseModel):
    customer_id: str = Field(..., description="Unique customer identifier")
    customer_name: str = Field(..., description="Company name")
    nps_score: int = Field(..., ge=0, le=10, description="NPS score (0-10)")
    open_tickets: int = Field(..., ge=0, description="Number of open support tickets")
    days_since_contact: int = Field(..., ge=0, description="Days since last contact")
    usage_trend: str = Field(default="Stable", description="Usage trend: Increasing, Stable, or Declining")

class ViabilityRequest(BaseModel):
    customer_id: str = Field(..., description="Unique customer identifier")
    customer_name: str = Field(..., description="Company name")
    setup_hours: int = Field(..., ge=0, description="Hours required for setup")
    monthly_revenue_eur: float = Field(..., gt=0, description="Monthly revenue in EUR")

class AgentResponse(BaseModel):
    agent_id: str
    customer_id: str
    customer_name: str
    response: str
    usage: Dict[str, int]
    cost_eur: float
    latency_ms: int
    timestamp: str

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for Cloud Run and monitoring"""
    return {
        "status": "healthy",
        "service": "groq-agent-router-mvp",
        "version": "1.0.0",
        "groq_api_configured": bool(GROQ_API_KEY),
        "timestamp": datetime.utcnow().isoformat()
    }

# Metrics endpoint
@app.get("/v1/metrics")
async def get_metrics():
    """Return service metrics for monitoring"""
    return {
        "total_invocations": 0,
        "total_tokens_used": 0,
        "estimated_cost_eur": 0.0,
        "using_free_credits": True,
        "actual_cost_eur": 0.0
    }

# List agents endpoint
@app.get("/v1/agents")
async def list_agents():
    """List all available agents"""
    return {
        "agents": [
            {
                "id": "customersat-construction-mvp",
                "name": "Customer Satisfaction Agent - Construction MVP",
                "type": "customer_satisfaction",
                "vertical": "construction",
                "model": "llama-3.1-70b-versatile",
                "status": "active"
            },
            {
                "id": "viability-construction-mvp",
                "name": "Viability Agent - Construction MVP",
                "type": "viability",
                "vertical": "construction",
                "model": "llama-3.1-70b-versatile",
                "status": "active"
            }
        ]
    }

@app.post("/v1/agents/customersat-construction-mvp/analyze", response_model=AgentResponse)
async def analyze_customer_health(request: CustomerHealthRequest):
    """Customer Satisfaction Agent - Analyzes customer health and churn risk"""
    
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY not configured")
    
    import time
    start_time = time.time()
    
    system_prompt = """You are a Customer Satisfaction Specialist for construction SMEs in the Nordic region.

ANALYZE these metrics:
1. NPS score (target: ≥8 healthy, 7 medium, ≤6 high risk)
2. Support tickets (>5 open = red flag)
3. Last contact (>30 days = issue, >45 days = high risk)
4. Usage trend (Declining = concerning)

OUTPUT (JSON only):
{
  "customer_id": "string",
  "customer_name": "string",
  "health_score": 0-100,
  "risk_level": "Low" | "Medium" | "High",
  "primary_concern": "main issue in one sentence",
  "recommended_action": "specific CSM action",
  "supporting_data": {"nps_score": N, "open_tickets": N, "days_since_contact": N}
}

Keep under 200 tokens. Be specific and actionable."""

    user_message = f"""Analyze: {request.customer_name} (ID: {request.customer_id})
NPS: {request.nps_score}/10
Tickets: {request.open_tickets}
Days since contact: {request.days_since_contact}
Trend: {request.usage_trend}"""

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                GROQ_API_URL,
                headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": "llama-3.1-70b-versatile",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 500
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=502, detail=f"Groq API error: {response.text}")
            
            result = response.json()
            agent_response = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            latency_ms = int((time.time() - start_time) * 1000)
            
            return AgentResponse(
                agent_id="customersat-construction-mvp",
                customer_id=request.customer_id,
                customer_name=request.customer_name,
                response=agent_response,
                usage=usage,
                cost_eur=0.0,
                latency_ms=latency_ms,
                timestamp=datetime.utcnow().isoformat()
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/agents/viability-construction-mvp/analyze", response_model=AgentResponse)
async def analyze_viability(request: ViabilityRequest):
    """Viability Agent - Calculates payback period and unit economics"""
    
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY not configured")
    
    import time
    start_time = time.time()
    
    system_prompt = """You are a Financial Analyst for construction SaaS.

CONSTANTS:
- Hardware: €700 (2× Jetson Nano)
- Setup rate: €80/hour
- Monthly COGS: €50

CALCULATE:
- Upfront = 700 + (hours × 80)
- Monthly GP = Revenue - 50
- Payback = Upfront / Monthly GP
- Margin % = (Revenue - 50) / Revenue × 100

RULES:
- Payback ≤2.0 → "Approve" ✅
- Payback 2.0-3.0 → "Review" ⚠️
- Payback >3.0 → "Reject" ❌

OUTPUT (JSON):
{
  "customer_id": "string",
  "customer_name": "string",
  "payback_months": number,
  "gross_margin_percent": number,
  "verdict": "Approve" | "Review" | "Reject",
  "calculation": "formula shown",
  "reasoning": "one sentence"
}"""

    user_message = f"""Calculate for: {request.customer_name}
Setup hours: {request.setup_hours}
Monthly revenue: €{request.monthly_revenue_eur}"""

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                GROQ_API_URL,
                headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": "llama-3.1-70b-versatile",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    "temperature": 0.1,
                    "max_tokens": 400
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=502, detail=f"Groq API error: {response.text}")
            
            result = response.json()
            agent_response = result["choices"][0]["message"]["content"]
            usage = result.get("usage", {})
            latency_ms = int((time.time() - start_time) * 1000)
            
            return AgentResponse(
                agent_id="viability-construction-mvp",
                customer_id=request.customer_id,
                customer_name=request.customer_name,
                response=agent_response,
                usage=usage,
                cost_eur=0.0,
                latency_ms=latency_ms,
                timestamp=datetime.utcnow().isoformat()
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "DWS IQ Agent Router - MVP",
        "version": "1.0.0",
        "documentation": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8083)
