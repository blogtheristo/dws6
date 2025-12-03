# DWS6 Pilot - AI Agent Router (MVP)

**FastAPI service with 2 AI agents for Nordic construction customer analysis**

## 🎯 Quick Start

### Prerequisites

- Python 3.11+
- Docker (optional, for containerized deployment)
- Groq API key
- Google Cloud account (for production deployment)

### Local Development

```bash
# 1. Install dependencies
cd AgentFoundry/services/groq-router-mvp
pip install -r requirements.txt

# 2. Set environment variables
export GROQ_API_KEY="your_groq_api_key_here"

# 3. Run the service
python main.py

# Service will start at http://localhost:8083
```

### Test Locally

```bash
# Health check
curl http://localhost:8083/health

# List available agents
curl http://localhost:8083/v1/agents

# Test Customer Satisfaction Agent
curl -X POST http://localhost:8083/v1/agents/customersat-construction-mvp/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "test_001",
    "customer_name": "Test Company",
    "nps_score": 8,
    "open_tickets": 2,
    "days_since_contact": 15,
    "usage_trend": "Stable"
  }'

# Test Viability Agent
curl -X POST http://localhost:8083/v1/agents/viability-construction-mvp/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "test_001",
    "customer_name": "Test Company",
    "setup_hours": 6,
    "monthly_revenue_eur": 750
  }'
```

## 🤖 Available Agents

### 1. Customer Satisfaction Agent

**Endpoint:** `POST /v1/agents/customersat-construction-mvp/analyze`

**Purpose:** Analyzes customer health metrics and identifies churn risk

**Input:**
```json
{
  "customer_id": "string",
  "customer_name": "string",
  "nps_score": 0-10,
  "open_tickets": number,
  "days_since_contact": number,
  "usage_trend": "Increasing|Stable|Declining"
}
```

**Output:**
```json
{
  "customer_id": "string",
  "health_score": 0-100,
  "risk_level": "Low|Medium|High",
  "primary_concern": "string",
  "recommended_action": "string"
}
```

### 2. Viability Agent

**Endpoint:** `POST /v1/agents/viability-construction-mvp/analyze`

**Purpose:** Calculates customer payback period and unit economics

**Input:**
```json
{
  "customer_id": "string",
  "customer_name": "string",
  "setup_hours": number,
  "monthly_revenue_eur": number
}
```

**Output:**
```json
{
  "customer_id": "string",
  "payback_months": number,
  "gross_margin_percent": number,
  "verdict": "Approve|Review|Reject",
  "calculation": "string"
}
```

## 🚀 Deployment

### Google Cloud Run (Production)

```bash
# 1. Set up Google Cloud project
cd /home/user/dws6
./scripts/setup_gcp.sh

# 2. Deploy service
./scripts/deploy.sh

# 3. Map custom domain (optional)
gcloud run domain-mappings create \
  --service groq-agent-router-mvp \
  --domain api.dws6.com \
  --region europe-north1
```

### GitHub Actions (Automated)

Push to `main` or `claude/dws6-pilot-setup-01MsouoNp4hdrFQxeYU6EJFY` branch to trigger automatic deployment.

## 📊 Test with 5 Nordic Companies

```bash
# Run test script with all 5 Nordic construction companies
cd /home/user/dws6
./scripts/test_agents.sh
```

**Companies included:**
1. Veidekke Entreprenør AS (Norway) - Healthy
2. Skanska Sverige AB (Sweden) - Medium Risk
3. YIT Rakennus Oy (Finland) - High Risk
4. NCC Construction Denmark A/S (Denmark) - Healthy
5. Peab Asfalt AB (Sweden) - Borderline

## 💰 Cost

**Local/Development:** €0
**Production (30 days):** €0 (using Groq free credits + GCP free tier)

- Groq API: €0 (using credits)
- Google Cloud Run: €0 (free tier: 2M requests/month)
- Total: **€0**

## 🔗 API Documentation

Interactive API docs available at:
- **Local:** http://localhost:8083/docs
- **Production:** https://your-service-url.run.app/docs

## 📝 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | ✅ | Groq API key for LLM inference |
| `SUPABASE_URL` | ❌ | Supabase project URL (optional) |
| `SUPABASE_KEY` | ❌ | Supabase anon key (optional) |
| `SLACK_WEBHOOK_URL` | ❌ | Slack webhook for notifications (optional) |

## 🛠️ Development

### Project Structure

```
groq-router-mvp/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Container configuration
├── .env.example        # Environment template
├── test_data/          # Mock Nordic companies
│   ├── NORDIC_CUSTOMERS.md
│   ├── NORDIC_COMPANIES_SCORED.md
│   ├── customer_001_health.json
│   ├── customer_001_viability.json
│   └── ...
└── README.md           # This file
```

### Adding New Agents

1. Add agent configuration in `main.py`
2. Create endpoint following existing pattern
3. Define Pydantic models for request/response
4. Add system prompt for agent behavior
5. Test locally before deploying

## 🐛 Troubleshooting

**Issue:** `GROQ_API_KEY not configured`
```bash
# Solution: Set environment variable
export GROQ_API_KEY="your_key_here"
```

**Issue:** `Groq API error: 401`
```bash
# Solution: Check API key is valid
curl https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer $GROQ_API_KEY"
```

**Issue:** `Docker build fails`
```bash
# Solution: Check Docker is running
docker version
```

## 📚 Next Steps

1. ✅ Deploy to Google Cloud Run
2. ✅ Map custom domain (api.dws6.com)
3. ✅ Set up Supabase database
4. ✅ Test with 5 Nordic companies
5. ⏳ Schedule investor demo
6. ⏳ Prepare case study materials

## 📞 Support

- **GitHub Issues:** [blogtheristo/dws6/issues](https://github.com/blogtheristo/dws6/issues)
- **Documentation:** `/home/user/dws6/GOOGLE_CLOUD_PILOT_PLAN.md`

---

**Version:** 1.0.0
**Last Updated:** December 3, 2025
**License:** Proprietary - Lifetime Oy
