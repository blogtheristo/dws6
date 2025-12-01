# Agent Configuration System

This directory contains agent configurations for the DWS IQ Platform's multi-agent system.

## Directory Structure

```
configs/
├── templates/          # Reusable agent templates
│   ├── customer-satisfaction-agent.yaml
│   ├── viability-agent.yaml
│   ├── deal-flow-agent.yaml (coming soon)
│   └── desirability-agent.yaml (coming soon)
│
└── instances/          # Deployed agent instances
    ├── customersat-construction-001.yaml
    ├── customersat-manufacturing-001.yaml
    ├── viability-construction-001.yaml
    └── ... (32 total instances)
```

## Agent Types

### 1. Customer Satisfaction Agent
- **Purpose:** Monitor customer health and prevent churn
- **Model:** Claude Sonnet 4.5
- **Key Metrics:** NPS, health score, engagement
- **Template:** `templates/customer-satisfaction-agent.yaml`

### 2. Viability Agent
- **Purpose:** Calculate unit economics and payback periods
- **Model:** Claude Sonnet 4.5 (low temperature for accuracy)
- **Key Metrics:** Payback period, gross margin, NRR, LTV/CAC
- **Template:** `templates/viability-agent.yaml`

### 3. Deal Flow Agent (Coming Soon)
- **Purpose:** Qualify leads and prioritize sales pipeline
- **Model:** Claude Sonnet 4.5

### 4. Desirability Agent (Coming Soon)
- **Purpose:** Market intelligence and competitive analysis
- **Model:** Claude Sonnet 4.5

## Creating a New Agent Instance

1. **Copy Template:**
   ```bash
   cp templates/customer-satisfaction-agent.yaml \
      instances/customersat-{VERTICAL}-001.yaml
   ```

2. **Customize Configuration:**
   - Replace `{VERTICAL}` with: construction, manufacturing, energy, etc.
   - Set deployment start dates for each phase
   - Configure integrations (HubSpot, Slack, etc.)

3. **Deploy to Cloud Run:**
   - Upload to Cloud Storage: `gs://lifetime-agent-configs/`
   - Restart `claude-agent-router` service

## Configuration Format

All agent configs use YAML format with these sections:

```yaml
agent:
  id: "unique-agent-id"
  name: "Human-readable name"
  type: "customer_satisfaction" | "viability" | "deal_flow" | "desirability"
  vertical: "construction" | "manufacturing" | etc.

  model:
    provider: "anthropic" | "groq"
    name: "claude-sonnet-4.5" | "llama-3.1-70b-versatile"
    temperature: 0.1-1.0

  system_prompt: |
    Agent behavior instructions...

  knowledge_base:
    - type: "vector_db" | "api" | "database" | "file"
      ...

  deployment:
    phase_1: {...}
    phase_2: {...}
    phase_3: {...}

  tools:
    - name: "tool_name"
      ...

  integrations:
    hubspot: {...}
    slack: {...}
    ...
```

## Template Variables

Templates use these placeholder variables:

- `{VERTICAL}` - Industry vertical (construction, manufacturing, etc.)
- `{PHASE_1_START_DATE}` - Phase 1 deployment date (YYYY-MM-DD)
- `{PHASE_2_START_DATE}` - Phase 2 deployment date
- `{PHASE_3_START_DATE}` - Phase 3 deployment date
- `{FINANCIAL_MODEL_SHEET_ID}` - Google Sheets ID for financial model

## Deployment Phases

All agents follow a 3-phase deployment:

### Phase 1: Silent Pilot (30 days)
- Observe and learn
- No autonomous actions
- Generate daily reports
- Calibrate accuracy

### Phase 2: Advisor Mode (60 days)
- Recommend actions
- Human approval required
- Activate dashboards
- Collect feedback

### Phase 3: Autonomous Mode
- Full automation
- Minimal human oversight
- CRM integration
- Proactive engagement

## Next Steps

1. Create remaining templates:
   - [ ] `deal-flow-agent.yaml`
   - [ ] `desirability-agent.yaml`

2. Deploy instances for all 8 verticals:
   - [ ] Construction (4 agents)
   - [ ] Manufacturing (4 agents)
   - [ ] Energy (4 agents)
   - [ ] Logistics (4 agents)
   - [ ] Real Estate (4 agents)
   - [ ] Architecture (4 agents)
   - [ ] Waste Management (4 agents)
   - [ ] Mining (4 agents)

## Resources

- [Deployment Guide](../DEPLOYMENT_GUIDE.md)
- [Rovo Analysis & Alternatives](../../ROVO_ANALYSIS_AND_ALTERNATIVES.md)
- [AgentFoundry README](../README.md)
