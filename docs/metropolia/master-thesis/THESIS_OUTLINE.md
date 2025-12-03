# Master's Thesis: Operating Model of Firehorse Product Manufacturing
**Metropolia University of Applied Sciences**

---

## Thesis Information

**Title:** Operating Model of Firehorse Product Manufacturing: A Hybrid AI-Edge Architecture for Climate-Intelligent Industrial Platforms

**Student:** Risto Anton Päärni
**Program:** [To be determined - likely Business IT or Industrial Management]
**Supervisor:** [TBD]
**Company:** Lifetime Oy (Firehorse brand)
**Thesis Type:** Implementation-based / Product Development
**Timeline:** [TBD - typically 6 months]

---

## 1. Research Problem & Objectives

### 1.1 Background

European industrial SMEs face a "twin transition" challenge:
- **Digital transformation**: AI, automation, real-time decisioning
- **Green transformation**: EU Fit for 55 (55% emissions reduction by 2030), embodied carbon mandates by 2028

Traditional SaaS platforms fail because they:
1. Cost €1,400+/month (unaffordable for SMEs)
2. Require cloud-only architecture (high latency, high operational costs)
3. Don't address industry-specific compliance workflows

**Firehorse (DWS6)** solves this with a novel operating model combining:
- Free-tier cloud infrastructure (€0-350/month vs €1,400+)
- Edge AI (NVIDIA Jetson) for <100ms inference
- Industry-specific AI agents (Construction, Manufacturing, Energy)
- Phased deployment (Silent Pilot → Advisor → Autonomous)

### 1.2 Research Questions

**Primary RQ:**
*How can a bootstrapped industrial AI platform achieve product-market fit through a hybrid cloud-edge operating model while maintaining <€400/month operational costs?*

**Secondary RQs:**
1. What cost structure enables viable SaaS for SMEs in regulated industries (construction, manufacturing)?
2. How does edge AI deployment (NVIDIA Jetson) create competitive moats vs cloud-only competitors?
3. What phased deployment model (Silent → Advisor → Autonomous) maximizes customer trust and retention in high-risk industries?
4. How can startup credits (AWS, Google, Groq) fund 6+ years of infrastructure without external capital?

### 1.3 Thesis Objectives

**Primary Objective:**
Document and validate the DWS6 operating model as a replicable framework for industrial AI product manufacturing.

**Deliverables:**
1. **Operating Model Canvas** (business model + technical architecture)
2. **Cost Model** (MVP → Alpha → V1 with actual figures)
3. **Deployment Playbook** (phased rollout for construction, manufacturing, energy)
4. **ROI Calculator** (customer payback period, edge AI savings)
5. **Lessons Learned** (what worked, what failed, recommendations)

---

## 2. Theoretical Framework

### 2.1 Core Theories

#### A) Lean Startup & Customer Development (Eric Ries, Steve Blank)
- **MVP strategy**: DWS6 launches with 2 agents, 5 customers, €0 cost
- **Build-Measure-Learn**: Silent Pilot (observe) → Advisor (recommend) → Autonomous (execute)
- **Validated learning**: Each phase proves hypotheses before scaling

#### B) Platform Business Models (Parker, Van Alstyne, Choudary)
- **Multi-sided platform**: DWS6 connects industrial customers + data providers + hardware vendors
- **Network effects**: More verticals → more reusable agent templates → faster deployment
- **Value creation**: Edge AI moat (€333K/year cost avoidance) vs cloud-only competitors

#### C) Industry 5.0 & Human-Centric Manufacturing (EU Commission)
- **Sustainability**: Real-time embodied carbon tracking for EU compliance
- **Resilience**: Edge computing enables offline operation (critical for construction sites)
- **Human-centricity**: AI recommends, humans approve (Phase 2: Advisor Mode)

#### D) Edge Computing Economics (Shi et al., 2016)
- **Latency**: <100ms edge inference vs 500ms+ cloud
- **Cost**: One-time hardware (€1,084/site) vs recurring cloud fees (€555/month/site)
- **ROI**: Hardware payback in 1.95 months

### 2.2 Conceptual Model

```
┌─────────────────────────────────────────────────────────────┐
│                 FIREHORSE OPERATING MODEL                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐│
│  │  FREE TIER   │────▶│ HYBRID ARCH  │────▶│   PHASED    ││
│  │  BOOTSTRAP   │     │ (Cloud+Edge) │     │ DEPLOYMENT  ││
│  └──────────────┘     └──────────────┘     └─────────────┘│
│        │                     │                     │       │
│        ▼                     ▼                     ▼       │
│  €0-350/month         <100ms latency      Trust building  │
│  (startup credits)    (NVIDIA Jetson)     (3 phases)      │
│                                                             │
│  ────────────────────── OUTCOMES ─────────────────────────│
│  • Product-market fit with 5-100 customers                 │
│  • €333K/year edge AI savings vs competitors               │
│  • 6+ years runway without external funding                │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Methodology

### 3.1 Research Approach

**Type:** Action Research + Case Study
**Setting:** Lifetime Oy's DWS6 product development (Dec 2025 - Nov 2026)
**Data Collection:** Implementation artifacts, cost tracking, customer feedback

### 3.2 Data Sources

#### Primary Data
1. **Implementation Artifacts**
   - Agent configurations (YAML files in `AgentFoundry/configs/`)
   - Deployment scripts (Cloud Run, Groq API, Supabase)
   - Cost tracking spreadsheets (monthly burn rate)
   - GitHub commit history (development velocity)

2. **Customer Data** (MVP Phase: 5 customers)
   - Onboarding interviews (pain points, expectations)
   - Agent interaction logs (what questions customers ask)
   - NPS scores and churn metrics
   - Payback period calculations (actual vs predicted)

3. **Operational Metrics**
   - Infrastructure costs (actual vs budgeted)
   - Agent response times (cloud vs edge)
   - Uptime and reliability (99%+ target)
   - Development velocity (features shipped per month)

#### Secondary Data
1. **Industry Reports**
   - EU construction market size and regulations
   - Manufacturing SME digital transformation trends
   - Edge computing adoption in industrial IoT

2. **Competitor Analysis**
   - Atlassian Rovo pricing and limitations
   - Traditional industrial SaaS (SAP, Siemens)
   - Cloud-only AI platforms (OpenAI, Anthropic)

### 3.3 Analysis Methods

1. **Cost-Benefit Analysis**
   - Compare DWS6 (€0-350/month) vs Rovo (€1,400/month)
   - Calculate edge AI ROI (hardware cost vs cloud savings)
   - Model customer payback period (≤2 months target)

2. **Thematic Analysis** (customer interviews)
   - Code interview transcripts for pain points, feature requests
   - Identify patterns across construction vs manufacturing verticals
   - Map findings to deployment phase (Silent → Advisor → Autonomous)

3. **Process Mapping**
   - Document agent development workflow (design → config → deploy → monitor)
   - Map customer journey (onboarding → pilot → production)
   - Identify bottlenecks and optimization opportunities

### 3.4 Validation

**Internal Validation:**
- Weekly reviews with Lifetime Oy team
- GitHub Projects tracking (Kanban % completion)
- Automated cost alerts (if >€400/month)

**External Validation:**
- Customer satisfaction (NPS ≥30)
- Investor feedback (target: €150K SAFE raise)
- Metropolia supervisor approval

---

## 4. Thesis Structure

### Chapter 1: Introduction
1.1 Background: EU twin transition (digital + green)
1.2 Research problem: Affordable industrial AI for SMEs
1.3 Research questions
1.4 Thesis scope and limitations
1.5 Key concepts and definitions

### Chapter 2: Theoretical Framework
2.1 Lean Startup and MVP methodology
2.2 Platform business models
2.3 Industry 5.0 and human-centric manufacturing
2.4 Edge computing economics
2.5 Conceptual model: Firehorse Operating Model Canvas

### Chapter 3: Current State Analysis
3.1 European industrial AI landscape
3.2 Competitor analysis (Rovo, SAP, Siemens)
3.3 Customer segments (construction, manufacturing, energy)
3.4 Regulatory drivers (EU Fit for 55, embodied carbon mandates)

### Chapter 4: DWS6 Operating Model Design
4.1 **Technical Architecture**
- Hybrid cloud-edge design (Google Cloud Run + NVIDIA Jetson)
- Agent system (Corporate Cloud Agents + SiteSense)
- Data flow (Supabase + AWS S3)

4.2 **Cost Model**
- Free tier bootstrap strategy (Groq, Google, AWS credits)
- Phased cost evolution (€0 → €50-150 → €350)
- Edge AI ROI (€333K/year savings)

4.3 **Deployment Model**
- Phase 1: Silent Pilot (observe, log, no actions)
- Phase 2: Advisor (recommend with approval)
- Phase 3: Autonomous (execute within guardrails)

4.4 **Go-to-Market Strategy**
- MVP: 5 construction customers, FREE pilot
- Alpha: 20-50 customers, 3 verticals
- V1: 100+ customers, 8 verticals

### Chapter 5: Implementation (MVP Phase)
5.1 Infrastructure deployment
- Cloud Run setup (Groq API router)
- Supabase configuration
- Monitoring and alerting

5.2 Agent development
- Customer Satisfaction Agent (Construction)
- Viability Agent (Construction)
- YAML configurations and testing

5.3 Customer onboarding
- 5 pilot customers (selection criteria)
- Onboarding workflow
- Training and support

5.4 Results
- Cost tracking (actual vs €0 budget)
- Agent performance (response time, accuracy)
- Customer feedback (NPS, testimonials)

### Chapter 6: Results & Analysis
6.1 **Cost Analysis**
- Actual costs vs budget (MVP, Alpha, V1)
- Edge AI savings validation
- Startup credits utilization

6.2 **Customer Analysis**
- Payback period (actual vs ≤2 month target)
- NPS scores and churn
- Feature requests and roadmap impact

6.3 **Operational Analysis**
- Development velocity (features per month)
- Infrastructure uptime
- Incident response and learnings

6.4 **Competitive Positioning**
- DWS6 vs Rovo (cost, features, flexibility)
- Edge AI moat vs cloud-only competitors
- Market validation (investor interest)

### Chapter 7: Discussion
7.1 Key findings and implications
7.2 Replicability: Can other startups use this model?
7.3 Limitations and threats
7.4 Recommendations for Lifetime Oy
7.5 Future research directions

### Chapter 8: Conclusions
8.1 Summary of research questions answered
8.2 Contribution to theory (Lean Startup, Platform Economics, Edge Computing)
8.3 Contribution to practice (operating model template)
8.4 Personal reflection

---

## 5. Expected Contributions

### 5.1 Theoretical Contributions

1. **Free-Tier Bootstrap Model**
   - Demonstrates how startup credits can fund 6+ years of infrastructure
   - Extends Lean Startup theory to capital-intensive industrial AI

2. **Hybrid Cloud-Edge Economics**
   - Validates edge AI ROI in real-world industrial deployment
   - Provides cost model template for hardware vs cloud tradeoffs

3. **Phased Trust-Building Framework**
   - Maps deployment phases (Silent → Advisor → Autonomous) to customer adoption curve
   - Shows how to de-risk AI in regulated, high-stakes industries

### 5.2 Practical Contributions

1. **Operating Model Template**
   - Reusable blueprint for bootstrapped industrial AI startups
   - Cost calculator, deployment checklist, agent configuration templates

2. **Industry-Specific Playbooks**
   - Construction vertical: Embodied carbon tracking, supplier risk
   - Manufacturing vertical: Energy optimization, waste routing
   - Transferable to energy, logistics, agriculture

3. **Open Source Agent Library**
   - YAML configurations for 33 agents across 8 verticals
   - FastAPI router for Groq API integration
   - Monitoring and alerting templates

---

## 6. Timeline & Milestones

### Month 1-2: Literature Review & Current State
- ☐ Review Lean Startup, Platform Economics, Industry 5.0 literature
- ☐ Analyze competitors (Rovo, SAP, Siemens)
- ☐ Interview 10 construction/manufacturing SMEs (pain points)
- ☐ **Deliverable:** Chapter 2 (Theory) + Chapter 3 (Current State)

### Month 3: Operating Model Design
- ☐ Document technical architecture (diagrams, data flows)
- ☐ Finalize cost model (free tier strategy, edge ROI)
- ☐ Design deployment phases (Silent, Advisor, Autonomous)
- ☐ **Deliverable:** Chapter 4 (Operating Model Design)

### Month 4-5: MVP Implementation
- ☐ Deploy infrastructure (Cloud Run, Supabase)
- ☐ Build 2 agents (Customer Sat, Viability)
- ☐ Onboard 5 pilot customers
- ☐ Collect data (costs, performance, feedback)
- ☐ **Deliverable:** Chapter 5 (Implementation)

### Month 6: Analysis & Writing
- ☐ Analyze cost data (actual vs budget)
- ☐ Analyze customer data (payback, NPS, churn)
- ☐ Compare DWS6 vs competitors
- ☐ Write Chapters 6 (Results), 7 (Discussion), 8 (Conclusions)
- ☐ **Deliverable:** Full thesis draft

### Month 7: Finalization
- ☐ Supervisor review and revisions
- ☐ Format and proofread
- ☐ Prepare defense presentation
- ☐ **Deliverable:** Final thesis + defense

---

## 7. Risk Management

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| MVP costs exceed €0 budget | Medium | High | Monitor costs weekly, use alerts, optimize queries |
| <5 pilot customers recruited | Medium | High | Start outreach early, offer free 60-day trial |
| Edge AI hardware delayed | Low | Medium | Start with cloud-only, add edge in Alpha phase |
| Competitor launches similar product | Low | Low | Focus on execution speed, edge AI moat |
| Thesis scope too broad | High | Medium | Limit to MVP phase (Month 1-3), defer Alpha/V1 to appendix |

---

## 8. References (Initial)

### Academic Literature
1. Ries, E. (2011). *The Lean Startup*. Crown Business.
2. Blank, S. (2013). *The Four Steps to the Epiphany*. K&S Ranch.
3. Parker, G., Van Alstyne, M., & Choudary, S. (2016). *Platform Revolution*. W.W. Norton.
4. European Commission (2021). *Industry 5.0: Towards a sustainable, human-centric and resilient European industry*.
5. Shi, W., et al. (2016). "Edge Computing: Vision and Challenges." *IEEE Internet of Things Journal*, 3(5), 637-646.

### Industry Reports
1. European Commission (2025). "Analysis of Life-Cycle GHG Emissions of EU Buildings." Ramboll.
2. GRESB (2024). "Establishing an Embodied Carbon Strategy in the EU Market."
3. Eurofound & Cedefop (2025). "SME Digitalisation in the EU: Trends, Policies and Impacts."
4. Statista (2024). "Revenue of Selected Large Construction Firms in Europe 2023."

### Technical Documentation
1. Atlassian Rovo Documentation: https://www.atlassian.com/software/rovo
2. NVIDIA Jetson Orin Technical Reference: https://developer.nvidia.com/jetson
3. Groq API Documentation: https://groq.com/docs
4. Google Cloud Run Pricing: https://cloud.google.com/run/pricing

---

## 9. Appendices (Planned)

**Appendix A:** Operating Model Canvas (full visual)
**Appendix B:** Agent Configuration Templates (YAML)
**Appendix C:** Cost Calculator (Google Sheets)
**Appendix D:** Customer Interview Protocol
**Appendix E:** Competitor Feature Comparison Matrix
**Appendix F:** GitHub Projects Screenshots (Kanban boards)
**Appendix G:** Weekly Report Template (English + Finnish)

---

**Document Status:** Draft v1.0
**Last Updated:** December 3, 2025
**Next Review:** [TBD with Metropolia supervisor]
