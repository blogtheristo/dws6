# AgentFoundry

**Agent Framework and Deployment Scripts**

This directory contains deployment scripts and frameworks for managing AI agents across different industries and use cases.

## Structure

```
AgentFoundry/
├── README.md                    # This file
├── Architecture/                # Architecture industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── Construction/                # Construction industry agents
│   ├── create-SiteSense Agent.csv          # Industry-specific edge AI agent
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── Energy/                      # Energy industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── Logistics/                   # Logistics industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── Manufacturing/               # Manufacturing industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── Mining/                      # Mining industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── RealEstate/                 # Real Estate industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
├── Waste/                       # Waste Management industry agents
│   ├── create-Customer Satisfaction Agent.csv
│   ├── create-Desirability Agent.csv
│   ├── create-Deal Flow Agent.csv
│   └── create-Viability Agent.csv
└── InvestorAgents/             # Investor relations and client acquisition agents
    ├── README.md
    ├── create-Investor Client Acquisition Agent.csv
    └── peachscore-guidelines.md
```

## Purpose

AgentFoundry provides a structured approach to:
- **Agent Deployment**: Scripts and configurations for deploying AI agents
- **Phased Rollouts**: Gradual deployment strategies to ensure reliability
- **Industry-Specific Agents**: Organized by industry vertical
- **Deployment Tracking**: Clear phases and goals for each agent rollout
- **Corporate Cloud Agents**: Three specialized agents per industry (Customer Satisfaction, Desirability, Deal Flow)
- **Investor Relations**: Agents for investor network and client acquisition via Peachscore

---

## Corporate Cloud Agents Overview

Each of the 8 industries receives four specialized **Corporate Cloud Agents** (formerly Background Agents):

1. **Customer Satisfaction Agent**: Monitors and improves customer satisfaction metrics, tracks NPS, handles feedback loops
2. **Desirability Agent**: Analyzes market desirability, competitive positioning, product-market fit indicators
3. **Deal Flow Agent**: Manages sales pipeline, identifies qualified leads, tracks conversion metrics
4. **Viability Agent**: Tracks unit economics and financial viability metrics (ACV, gross margins, payback periods, capital intensity, CAC, LTV, pilot conversion rates, NRR), calculates viability scores (0-100), and flags red industries to feed into Deal Flow + Desirability agents

All agents follow a three-phase deployment model:
- **Phase 1**: Silent pilot / training phase
- **Phase 2**: Human-in-the-loop / advisory phase
- **Phase 3**: Autonomous / production phase

---

## Industry Agents

### Architecture Industry

**Market Size**: $300B+ global market, BIM and carbon tracking focus

**Agents**:
- **Customer Satisfaction Agent**: Monitors client feedback, project satisfaction, and stakeholder engagement
- **Desirability Agent**: Analyzes design trends, market positioning, and competitive landscape
- **Deal Flow Agent**: Manages architecture project pipeline, client acquisition, and proposal tracking
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for architecture industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Construction Industry

**Market Size**: 3.5 million construction companies in Europe

**Agents**:
- **SiteSense Agent**: AI-powered edge computing system for construction site monitoring, material optimization, and predictive logistics
- **Customer Satisfaction Agent**: Monitors contractor satisfaction, project delivery quality, and stakeholder feedback
- **Desirability Agent**: Analyzes construction market trends, competitive positioning, and project desirability
- **Deal Flow Agent**: Manages construction project pipeline, bid tracking, and client acquisition
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback ≤ 2 months target, CAC, LTV, NRR) and calculates viability scores for construction industry

**SiteSense Agent Key Features**:
- **Real-time Monitoring**: <100ms latency edge inference
- **Computer Vision**: YOLO-based material detection and volumetric estimation
- **IoT Integration**: Sensor data aggregation from site equipment
- **Weather Intelligence**: API integration for predictive planning
- **Predictive Logistics**: Demand prediction engine with supplier integration

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Energy Industry

**Market Size**: $2T+ global market, accelerating renewable transition

**Agents**:
- **Customer Satisfaction Agent**: Monitors energy customer satisfaction, service quality, and retention metrics
- **Desirability Agent**: Analyzes renewable energy market trends, grid optimization opportunities, and competitive positioning
- **Deal Flow Agent**: Manages energy project pipeline, PPA negotiations, and client acquisition
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for energy industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Logistics Industry

**Market Size**: $8T global market, supply chain optimization critical

**Agents**:
- **Customer Satisfaction Agent**: Monitors logistics customer satisfaction, delivery performance, and service quality
- **Desirability Agent**: Analyzes supply chain trends, logistics market positioning, and competitive landscape
- **Deal Flow Agent**: Manages logistics contract pipeline, RFQ tracking, and client acquisition
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for logistics industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Manufacturing Industry

**Market Size**: $10T global industry, 2M+ manufacturing companies in Europe

**Agents**:
- **Customer Satisfaction Agent**: Monitors manufacturing customer satisfaction, product quality, and delivery performance
- **Desirability Agent**: Analyzes Industry 5.0 trends, manufacturing market positioning, and competitive landscape
- **Deal Flow Agent**: Manages manufacturing contract pipeline, OEM relationships, and client acquisition
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for manufacturing industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Mining Industry

**Market Size**: $1.5T global market, resource optimization critical

**Agents**:
- **Customer Satisfaction Agent**: Monitors mining customer satisfaction, safety metrics, and operational performance
- **Desirability Agent**: Analyzes mining market trends, resource optimization opportunities, and competitive positioning
- **Deal Flow Agent**: Manages mining project pipeline, contract negotiations, and client acquisition
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for mining industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Real Estate Industry

**Market Size**: $280T global asset value, smart building transformation

**Agents**:
- **Customer Satisfaction Agent**: Monitors tenant satisfaction, building performance, and property management metrics
- **Desirability Agent**: Analyzes real estate market trends, property desirability, and competitive positioning
- **Deal Flow Agent**: Manages real estate transaction pipeline, property acquisition, and client relationships
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for real estate industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

### Waste Management Industry

**Market Size**: $530B global market, circular economy acceleration

**Agents**:
- **Customer Satisfaction Agent**: Monitors waste management customer satisfaction, service quality, and recycling metrics
- **Desirability Agent**: Analyzes circular economy trends, waste-to-energy opportunities, and competitive positioning
- **Deal Flow Agent**: Manages waste management contract pipeline, municipal relationships, and client acquisition
- **Viability Agent**: Tracks unit economics (ACV, gross margins, payback, CAC, LTV, NRR) and calculates viability scores for waste management industry

**Deployment Timeline**: Q1 2026 (Pilot) → Q2 2026 (Advisory) → Q3 2026 (Autonomous)

---

## Viability Agent - Unit Economics & Financial Metrics

**Purpose**: Tracks unit economics and financial viability metrics per industry to ensure sustainable business model and flag red industries.

**Key Metrics Tracked**:

1. **ACV & Gross Margin per Customer**
   - Inputs: Price per month/year, COGS (infrastructure, support, hardware depreciation)
   - Output: Gross margin % and € per customer

2. **Payback Period on Hardware + Setup**
   - Inputs: Upfront Jetson + install cost, monthly gross profit from site
   - Output: Months to payback (target: ≤ 2 months, like the 1.95 month example)

3. **Capital Intensity per € of ARR**
   - Inputs: Total hardware + infrastructure capex for industry, ARR from industry
   - Output: Capex/ARR ratio (€ of hardware to support 1 € ARR)

4. **Sales Efficiency / CAC Proxy**
   - Inputs: Hours spent on sales + onboarding per deal (× blended €/hour), external costs (travel, tools)
   - Output: Effective CAC per customer and CAC payback in months (CAC / monthly gross profit)

5. **LTV per Customer Segment**
   - Inputs: Average contract length (or churn), average ACV, gross margin
   - Output: LTV = ACV × gross margin % × expected years

6. **Pilot → Production Conversion Rate**
   - Inputs: Number of pilots started, number converted to paying production customers
   - Output: % of pilots that convert, average time from pilot start to conversion

7. **Net Revenue Retention (NRR) per Industry**
   - Inputs: Starting ARR for cohort, upsell/expansion, downgrades, churn after 12 months
   - Output: NRR % (target > 100% if expansion modules exist)

**Agent Capabilities**:
- Pulls metrics monthly per industry
- Flags "red" industries where payback, CAC, or NRR fall below thresholds
- Calculates viability score (0-100) per industry
- Feeds scores into Deal Flow + Desirability agents to avoid bad-economics verticals

---

## Investor Agents

**Location**: `InvestorAgents/`

**Purpose**: AI-powered system for investor relations and client acquisition through Peachscore network.

**Agents**:
- **Investor Client Acquisition Agent**: Manages investor network relationships, warm introductions, and client acquisition via Peachscore guidelines

**Key Features**:
- **Peachscore Integration**: Benchmark against 500+ Finnish scaleups
- **Investor Network Access**: Direct connection to Nordic VCs (Lifeline Ventures, Inventure, etc.)
- **Warm Introductions**: Automated identification of best-fit investors via Peachscore community
- **Client Qualification**: AI-powered lead scoring based on Peachscore guidelines
- **Quarterly Events**: Automated tracking and participation in Peachscore meetups

**See**: `InvestorAgents/README.md` for full documentation and `InvestorAgents/peachscore-guidelines.md` for detailed guidelines.

---

## Usage

### Deploying Corporate Cloud Agents

Each industry has four standard agents that follow the same deployment pattern:

1. **Phase 1 - Silent Pilot**: Deploy agent to observe and learn without taking actions
2. **Phase 2 - Advisor Mode**: Activate dashboard for human review and approval
3. **Phase 3 - Autonomous Mode**: Full integration with systems for autonomous operation

### Adding a New Industry

1. Create a new industry folder (e.g., `NewIndustry/`)
2. Create four agent CSV files:
   - `create-Customer Satisfaction Agent.csv`
   - `create-Desirability Agent.csv`
   - `create-Deal Flow Agent.csv`
   - `create-Viability Agent.csv`
3. Follow the CSV format with Phase/Action/Goal structure
4. Document the industry in this README

### Deployment Script Format

All deployment scripts follow a phased approach:
- **Phase 1**: Silent pilot / training phase - Agent observes and learns
- **Phase 2**: Human-in-the-loop / advisory phase - Agent suggests, human approves
- **Phase 3**: Autonomous / production phase - Agent operates within set parameters

---

## Related Documentation

- **Investor Timeline**: See `../investor-timeline.md` for 2026 Corporate Cloud Agents rollout schedule across all 8 industries
- **Strategic Partnerships**: See `../STRATEGIC_PARTNERSHIPS.md` for Peachscore guidelines and investor network details
- **SiteSense Agent Details**: See `dws10.com/construction/index.html` for full product description
- **Architecture**: See `ARCHITECTURE_SUMMARY.md` for system architecture
- **Agent Framework**: See `lifetime-agent-foundry/AGENT_FOUNDRY.md` for development framework
- **Investor Agents**: See `InvestorAgents/README.md` for investor relations and client acquisition agents

---

## 2026 Corporate Cloud Agents Rollout Schedule

- **Q1 2026**: Construction & Manufacturing pilot launch (Customer Satisfaction Agents)
- **Q2 2026**: Energy & Logistics pilot launch; Real Estate & Architecture pilot launch; Waste & Mining pilot launch
- **Q3 2026**: Phase 2 activation (Advisor mode) for all industries
- **Q4 2026**: Phase 3 deployment (Autonomous mode) for all industries

See `investor-timeline.md` for detailed quarterly milestones and industry-specific timelines.

---

**Last Updated**: January 2026

