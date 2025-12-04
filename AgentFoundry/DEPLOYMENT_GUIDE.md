# AgentFoundry Deployment Guide

**Version:** 1.0.0
**Last Updated:** December 2025
**Target:** Claude + Groq Multi-Agent System on Google Cloud Run

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Architecture Overview](#architecture-overview)
3. [Local Development Setup](#local-development-setup)
4. [Deploying Claude Router Service](#deploying-claude-router-service)
5. [Creating Agent Instances](#creating-agent-instances)
6. [Testing Agents](#testing-agents)
7. [Deploying Workflows](#deploying-workflows)
8. [Monitoring & Observability](#monitoring--observability)
9. [Cost Management](#cost-management)
10. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Accounts & API Keys

- [x] **Anthropic API Key** - Get from [console.anthropic.com](https://console.anthropic.com)
- [x] **Groq API Key** - Already have $10K startup credits
- [x] **Google Cloud Project** - Already configured for Cloud Run
- [x] **Supabase Account** - Already configured with pgvector
- [x] **GitHub Repository** - blogtheristo/dws6

### Required Tools

```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
gcloud init

# Install Docker
# (Already installed on your system)

# Install Python 3.11+
python --version  # Should be 3.11+

# Install dependencies
pip install anthropic fastapi uvicorn pyyaml httpx
```

### Environment Variables

Create a `.env` file in `/home/user/dws6/AgentFoundry/`:

```bash
# API Keys
ANTHROPIC_API_KEY=sk-ant-...
GROQ_API_KEY=gsk_...

# Service URLs
GROQ_API_URL=http://groq-inference-proxy:8082
EDGE_SYNC_SERVICE_URL=http://edge-sync-service:8081

# Database
SUPABASE_CONNECTION_STRING=postgresql://postgres:...@db.xxx.supabase.co:5432/postgres

# Integrations
HUBSPOT_API_KEY=...
INTERCOM_API_KEY=...
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
STRIPE_API_KEY=sk_live_...

# Google Sheets (for financial models)
GOOGLE_SHEETS_CREDENTIALS_JSON='{...}'

# AWS (for cost data)
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Google Cloud Run                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌───────────┐ │
│  │ claude-agent-    │  │ groq-inference-  │  │ edge-sync │ │
│  │ router           │  │ proxy            │  │ service   │ │
│  │ (Port 8083)      │  │ (Port 8082)      │  │ (8081)    │ │
│  └──────────────────┘  └──────────────────┘  └───────────┘ │
│         ▲                       ▲                    ▲       │
│         │                       │                    │       │
└─────────┼───────────────────────┼────────────────────┼───────┘
          │                       │                    │
          │                       │                    │
    ┌─────▼───────┐         ┌────▼──────┐      ┌─────▼────────┐
    │ Claude API  │         │ Groq API  │      │ NVIDIA Jetson│
    │ (Anthropic) │         │ (Llama)   │      │ Edge Devices │
    └─────────────┘         └───────────┘      └──────────────┘

                      ┌─────────────────┐
                      │ Supabase        │
                      │ - Agent Configs │
                      │ - Knowledge Base│
                      │ - Audit Logs    │
                      └─────────────────┘
```

### Service Responsibilities

| Service | Port | Purpose | Technology |
|---------|------|---------|------------|
| **claude-agent-router** | 8083 | Routes requests to Claude or Groq | FastAPI + Anthropic SDK |
| **groq-inference-proxy** | 8082 | Proxies Groq API calls with rate limiting | FastAPI + Groq SDK |
| **edge-sync-service** | 8081 | Manages edge device sync | FastAPI + AWS IoT |
| **agent-orchestrator** | 8080 | Multi-agent workflows | LlamaStack |

---

## Local Development Setup

### 1. Clone Repository

```bash
cd /home/user/dws6/AgentFoundry
```

### 2. Install Dependencies

```bash
cd services/claude-router
pip install -r requirements.txt
```

### 3. Run Locally

```bash
# Set environment variables
export ANTHROPIC_API_KEY=sk-ant-...
export GROQ_API_URL=http://localhost:8082

# Start the service
python main.py
```

The service will start at `http://localhost:8083`.

### 4. Test Health Endpoint

```bash
curl http://localhost:8083/health
```

Expected output:
```json
{
  "status": "healthy",
  "service": "claude-agent-router",
  "timestamp": "2025-12-01T12:00:00.000000"
}
```

---

## Deploying Claude Router Service

### 1. Build Docker Image

```bash
cd /home/user/dws6/AgentFoundry/services/claude-router

# Build image
docker build -t claude-agent-router:latest .

# Tag for Google Container Registry
docker tag claude-agent-router:latest \
  europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/claude-agent-router:v1.0.0
```

### 2. Push to Google Container Registry

```bash
# Authenticate Docker with GCR
gcloud auth configure-docker

# Push image
docker push europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/claude-agent-router:v1.0.0
```

### 3. Deploy to Cloud Run

```bash
gcloud run deploy claude-agent-router \
  --image europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/claude-agent-router:v1.0.0 \
  --platform managed \
  --region europe-north1 \
  --port 8083 \
  --memory 1Gi \
  --cpu 1 \
  --min-instances 1 \
  --max-instances 10 \
  --set-env-vars ANTHROPIC_API_KEY=sk-ant-... \
  --set-env-vars GROQ_API_URL=https://groq-inference-proxy-xxx.run.app \
  --set-env-vars SUPABASE_CONNECTION_STRING=postgresql://... \
  --allow-unauthenticated
```

### 4. Verify Deployment

```bash
# Get service URL
export SERVICE_URL=$(gcloud run services describe claude-agent-router \
  --region europe-north1 \
  --format 'value(status.url)')

# Test health endpoint
curl $SERVICE_URL/health

# List agents
curl $SERVICE_URL/v1/agents
```

---

## Creating Agent Instances

### 1. Create Agent Configuration

Use the templates in `AgentFoundry/configs/templates/` to create agent instances.

**Example: Customer Satisfaction Agent for Construction**

```bash
cd /home/user/dws6/AgentFoundry/configs

# Copy template
cp templates/customer-satisfaction-agent.yaml \
   instances/customersat-construction-001.yaml
```

### 2. Customize Configuration

Edit `instances/customersat-construction-001.yaml`:

```yaml
agent:
  id: "customersat-construction-001"
  name: "Customer Satisfaction Agent - Construction"
  vertical: "construction"

  deployment:
    phase_1:
      start_date: "2026-01-15"
    phase_2:
      start_date: "2026-02-15"
    phase_3:
      start_date: "2026-04-15"
```

### 3. Upload Configuration to Cloud Run

**Option A: Bake configs into Docker image**

```dockerfile
# Add to Dockerfile
COPY configs/instances/ /app/configs/instances/
```

**Option B: Mount from Cloud Storage**

```bash
# Upload configs to Google Cloud Storage
gsutil -m cp -r configs/instances/ \
  gs://lifetime-agent-configs/

# Mount in Cloud Run (use gcloud beta)
gcloud beta run deploy claude-agent-router \
  --image europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/claude-agent-router:v1.0.0 \
  --execution-environment gen2 \
  --add-volume name=agent-configs,type=cloud-storage,bucket=lifetime-agent-configs \
  --add-volume-mount volume=agent-configs,mount-path=/app/configs/instances
```

### 4. Verify Agent is Loaded

```bash
curl $SERVICE_URL/v1/agents
```

Expected output:
```json
{
  "agents": [
    {
      "id": "customersat-construction-001",
      "name": "Customer Satisfaction Agent - Construction",
      "type": "customer_satisfaction",
      "vertical": "construction",
      "model": "claude-sonnet-4.5"
    }
  ]
}
```

---

## Testing Agents

### 1. Invoke Agent via API

```bash
curl -X POST $SERVICE_URL/v1/agents/customersat-construction-001/invoke \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Analyze customer health for customer_123. They have NPS score of 6, 3 open support tickets, and last interaction was 45 days ago."
      }
    ],
    "max_tokens": 4000
  }'
```

Expected output (example):
```json
{
  "id": "msg_01ABC...",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "{\"customer_id\":\"customer_123\",\"health_score\":42,\"risk_level\":\"High\",\"risk_factors\":[\"NPS below 7\",\"Multiple open tickets\",\"Low engagement (45 days)\"],\"recommended_actions\":[{\"action\":\"Schedule immediate check-in call\",\"urgency\":\"High\",\"owner\":\"CSM\"}],\"supporting_data\":{\"nps_score\":6,\"last_interaction_days\":45,\"open_tickets\":3,\"usage_trend\":\"Decreasing\"}}"
    }
  ],
  "model": "claude-sonnet-4.5",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 512,
    "output_tokens": 256
  }
}
```

### 2. Test Tool Calling

```bash
curl -X POST $SERVICE_URL/v1/agents/customersat-construction-001/invoke \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Get NPS scores for the construction segment over the last 30 days."
      }
    ]
  }'
```

The agent should respond with a tool use request:
```json
{
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_01ABC...",
      "name": "get_nps_scores",
      "input": {
        "segment": "construction",
        "days": 30
      }
    }
  ]
}
```

### 3. Execute Tool

```bash
curl -X POST $SERVICE_URL/v1/agents/customersat-construction-001/tools/execute \
  -H "Content-Type: application/json" \
  -d '{
    "tool_name": "get_nps_scores",
    "tool_input": {
      "segment": "construction",
      "days": 30
    }
  }'
```

---

## Deploying Workflows

### 1. Package Workflow

```bash
cd /home/user/dws6/AgentFoundry/workflows

# Create Dockerfile for workflow service
cat > Dockerfile <<EOF
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY customer_onboarding.py .
CMD ["python", "customer_onboarding.py"]
EOF

# Create requirements.txt
cat > requirements.txt <<EOF
httpx==0.26.0
python-dotenv==1.0.0
EOF
```

### 2. Deploy Workflow Service

```bash
# Build and push
docker build -t workflow-customer-onboarding:latest .
docker tag workflow-customer-onboarding:latest \
  europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/workflow-customer-onboarding:v1.0.0
docker push europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/workflow-customer-onboarding:v1.0.0

# Deploy to Cloud Run
gcloud run deploy workflow-customer-onboarding \
  --image europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/workflow-customer-onboarding:v1.0.0 \
  --region europe-north1 \
  --set-env-vars CLAUDE_ROUTER_URL=https://claude-agent-router-xxx.run.app \
  --set-env-vars EDGE_SYNC_SERVICE_URL=https://edge-sync-service-xxx.run.app
```

### 3. Trigger Workflow (Example)

Create a Cloud Run Job:

```bash
gcloud run jobs create onboard-customer \
  --image europe-north1-docker.pkg.dev/dws-iq-pilot/dws-containers/workflow-customer-onboarding:v1.0.0 \
  --region europe-north1 \
  --args="--customer-id=cust_123,--vertical=construction"
```

Execute:
```bash
gcloud run jobs execute onboard-customer --region europe-north1
```

---

## Monitoring & Observability

### 1. Google Cloud Logging

View logs in real-time:

```bash
gcloud logging tail "resource.type=cloud_run_revision AND \
  resource.labels.service_name=claude-agent-router"
```

### 2. Cost Tracking

Create a dashboard to track API costs:

```bash
# Query Claude API usage
gcloud logging read "resource.type=cloud_run_revision AND \
  jsonPayload.message=~'Claude API call'" \
  --format json | \
  jq '[.[] | .jsonPayload | {input_tokens, output_tokens}] |
      add |
      {input_tokens, output_tokens,
       cost_eur: ((.input_tokens / 1000000 * 3) + (.output_tokens / 1000000 * 15))}'
```

### 3. Grafana Dashboard

Create a dashboard with:
- Agent invocations per hour
- Average latency by agent type
- Cost per agent (input + output tokens)
- Health score distribution
- Approval rates (Phase 2)

**Supabase Queries:**

```sql
-- Agent invocations over time
SELECT
  DATE_TRUNC('hour', created_at) AS hour,
  agent_id,
  COUNT(*) AS invocations
FROM agent_actions_audit
WHERE created_at > NOW() - INTERVAL '24 hours'
GROUP BY hour, agent_id
ORDER BY hour DESC;

-- Cost tracking
SELECT
  agent_id,
  SUM(input_tokens) AS total_input_tokens,
  SUM(output_tokens) AS total_output_tokens,
  (SUM(input_tokens) / 1000000.0 * 3.0) +
  (SUM(output_tokens) / 1000000.0 * 15.0) AS cost_eur
FROM agent_actions_audit
WHERE created_at > NOW() - INTERVAL '30 days'
GROUP BY agent_id;
```

---

## Cost Management

### Monthly Budget Alert

Set up budget alerts:

```bash
gcloud billing budgets create \
  --billing-account=XXXXXX-XXXXXX-XXXXXX \
  --display-name="Claude API Monthly Budget" \
  --budget-amount=300EUR \
  --threshold-rule=percent=80 \
  --threshold-rule=percent=100
```

### Cost Optimization Tips

1. **Use Groq for high-volume tasks** - 1,250 tokens/sec at lower cost
2. **Cache system prompts** - Reduce input token usage by 50%
3. **Batch requests** - Group multiple customer analyses
4. **Lower temperature for deterministic tasks** - Fewer retries needed
5. **Use Phase 1 wisely** - Silent pilot doesn't send emails (lower API usage)

### Estimated Monthly Costs (32 Agents)

| Agent Type | Provider | Tokens/Month | Cost/Month |
|------------|----------|--------------|------------|
| Customer Sat (8 agents) | Claude | 4M | €72 |
| Viability (8 agents) | Claude | 6M | €108 |
| Deal Flow (8 agents) | Claude | 3M | €54 |
| Desirability (8 agents) | Claude | 2M | €36 |
| **TOTAL** | | **15M** | **€270** |

**Plus:**
- Groq API: €0 (covered by $10K credits)
- Cloud Run: ~€50/month (1Gi × 3 services × always-on)
- Supabase: €25/month (Pro tier)

**Grand Total: ~€345/month**

Compare to Rovo: €16,800/year (€1,400/month) for 100 users.

---

## Troubleshooting

### Agent Not Loading

**Error:** `Agent configuration not found for {agent_id}`

**Solution:**
1. Verify config file exists:
   ```bash
   ls /home/user/dws6/AgentFoundry/configs/instances/{agent_id}.yaml
   ```
2. Check file is mounted in Cloud Run
3. Restart Cloud Run service

### Claude API Rate Limit

**Error:** `429 Too Many Requests`

**Solution:**
1. Implement exponential backoff in `main.py`:
   ```python
   import time

   for attempt in range(3):
       try:
           response = claude_client.messages.create(...)
           break
       except anthropic.RateLimitError:
           time.sleep(2 ** attempt)
   ```
2. Increase `max-instances` in Cloud Run to distribute load

### High Costs

**Issue:** Monthly Claude API costs exceed budget

**Solution:**
1. Review top consumers:
   ```sql
   SELECT agent_id, SUM(input_tokens + output_tokens) AS total_tokens
   FROM agent_actions_audit
   GROUP BY agent_id
   ORDER BY total_tokens DESC;
   ```
2. Switch high-volume agents to Groq:
   - Edit agent config: `provider: "groq"`
   - Redeploy

### Tool Execution Fails

**Error:** `HTTPError: 401 Unauthorized` when calling external API

**Solution:**
1. Check API key environment variables
2. Verify API key scopes/permissions
3. Test API manually:
   ```bash
   curl -H "Authorization: Bearer $HUBSPOT_API_KEY" \
     https://api.hubspot.com/crm/v3/objects/contacts
   ```

---

## Next Steps

### Phase 1 Deployment (Month 1)

1. **Week 1-2:**
   - [x] Deploy `claude-agent-router` to Cloud Run
   - [ ] Create agent configs for Construction vertical (4 agents)
   - [ ] Test agents with sample data

2. **Week 3-4:**
   - [ ] Deploy Customer Sat Agent to 5 pilot sites
   - [ ] Set up Slack notifications
   - [ ] Daily report generation

### Phase 2 Activation (Month 2)

1. **Week 5-6:**
   - [ ] Deploy all 32 agents (4 types × 8 industries)
   - [ ] Set up approval workflows
   - [ ] Train CSMs on using agent recommendations

2. **Week 7-8:**
   - [ ] Activate Phase 2 for Customer Sat Agent
   - [ ] A/B test Claude vs. Groq performance
   - [ ] Collect feedback from users

### Phase 3 Autonomous (Month 3)

1. **Week 9-10:**
   - [ ] Deploy SiteSense Edge agents to 10 sites
   - [ ] Real-time edge-to-cloud sync

2. **Week 11-12:**
   - [ ] Activate Phase 3 autonomous mode
   - [ ] Investor demo preparation
   - [ ] ROI measurement & reporting

---

## Support & Resources

- **Documentation:** [AgentFoundry README](./README.md)
- **Architecture:** [ARCHITECTURE_SUMMARY.md](/home/user/dws6/ARCHITECTURE_SUMMARY.md)
- **GitHub Issues:** [blogtheristo/dws6/issues](https://github.com/blogtheristo/dws6/issues)
- **Slack Channel:** `#agent-ops` (internal)

---

**Last Updated:** December 1, 2025
**Maintained By:** Lifetime Oy AI Team
