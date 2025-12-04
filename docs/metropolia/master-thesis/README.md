# Metropolia Master's Thesis - DWS6 Operating Model
**Student:** Risto Anton Päärni | **Company:** Lifetime Oy (Firehorse)

---

## Folder Structure

```
docs/metropolia/master-thesis/
├── README.md (this file)
├── en/ (English artifacts)
│   ├── THESIS_OUTLINE.md
│   └── RESEARCH_FRAMEWORK.md
├── fi/ (Finnish artifacts - PRIMARY)
│   └── OPINNAYTETYO_SUUNNITELMA_FI.md
└── data-collection/ (to be created during MVP)
    ├── customer-interviews/
    ├── cost-tracking/
    └── weekly-logs/
```

---

## Language Policy

**Primary language:** Finnish (Suomi)
- Thesis will be written in Finnish for Metropolia
- Main document: `fi/OPINNAYTETYO_SUUNNITELMA_FI.md`

**Supporting language:** English
- Technical documentation and implementation guides in English
- English versions in `en/` folder for international reference

---

## Research Focus

**Industry:** Construction / Rakennusteollisuus

**Why construction?**
- Most developed model in DWS6
- Clear regulatory driver (EU embodied carbon mandate 2028)
- 5 Nordic pilot customers ready for MVP phase
- €74Bn+ market (Vinci, Bouygues, ACS, Strabag, Hochtief)

---

## Four Research Questions (Neljä tutkimuskysymystä)

### 1. Tuote ja liiketoimintamalli (Product & Business Model)
- Customer promise development (Asiakaslupauksen kehittäminen)
- Product vision (Tuotteen visio)
- Limited market research (Suppea markkinatutkimus)
- Problem definition (Minkä ongelman tuote ratkaisee?)

### 2. Teknologia - Monialustainen kehitys (Multi-platform Technology)
- Digital scalable service product (Digitaalinen skaalautuva palvelutuote)
- E-commerce implementation (Verkkokauppatoteutus)
- Marketing channel solutions (Markkinointikanavien ratkaisut)
- AI-based software implementation (Tekoälypohjainen ohjelmistototeutus)

### 3. Teknisten ratkaisujen evaluointi (Technical Solution Evaluation)
- **Solution 1:** Agents for Lifetime Firehorse DWS IQ as cloud-native app
- **Solution 2:** Websites, applications, automations
- **Solution 3:** Cursor AI + Docker MCP (development tools)

### 4. Yritysturvallisuus (Enterprise Security)
- NIS 2 / EU AI Act / GDPR / Cybersecurity Act compliance

---

## Key Technical Decisions

### MCP (Model Context Protocol) Status
**Tested but not in production:**
- MCP solutions were extensively tested for agent-to-agent communication
- **Only Docker MCP remains in use** with Cursor.AI development environment
- Not a significant role in final architecture

### Primary Technologies
- **Cloud:** Google Cloud Run (€0/month free tier MVP)
- **AI:** Groq Llama 3.1 70B + Claude Sonnet 4.5
- **Edge:** NVIDIA Jetson Orin Nano (€1,084/site, <100ms latency)
- **Development:** Cursor.AI + Docker MCP + GitHub Copilot

---

## Timeline

| Phase | Duration | Focus | Thesis Chapter |
|-------|----------|-------|----------------|
| **Lit Review** | Month 1-2 | Theory, competitors, market | Ch 2-3 |
| **Design** | Month 3 | Operating model, architecture | Ch 4 |
| **MVP Implementation** | Month 4-5 | 2 agents, 5 customers, €0 cost | Ch 5 |
| **Analysis** | Month 6 | Results, cost validation, ROI | Ch 6 |
| **Writing** | Month 6-7 | Discussion, conclusions | Ch 7-8 |
| **Defense** | Month 8 | Thesis presentation | - |

---

## Files Overview

### Finnish (PRIMARY)
- **OPINNAYTETYO_SUUNNITELMA_FI.md** (35,000+ words)
  - Complete thesis outline in Finnish
  - 4 research questions addressed
  - Construction industry focus
  - 8 chapters with detailed methodology

### English (REFERENCE)
- **THESIS_OUTLINE.md** (10,000+ words)
  - English version for international collaboration
  - Same structure as Finnish version

- **RESEARCH_FRAMEWORK.md** (8,000+ words)
  - Detailed methodology and data collection protocols
  - Interview protocols, cost tracking formulas
  - Validity, reliability, ethics

---

## Expected Contributions

### Theoretical
1. Free-Tier Bootstrap Model (6+ years runway with startup credits)
2. Hybrid Cloud-Edge Economics (€333K/year savings validation)
3. Phased Trust-Building Framework (Silent → Advisor → Autonomous)

### Practical
1. Operating Model Template (reusable for other construction tech startups)
2. Construction Industry Playbook (embodied carbon tracking, viability analysis)
3. Open Source Agent Library (YAML configs for 2 MVP agents)

---

## Data Collection (Starting MVP Phase)

**Week 1-12 (Dec 2025 - Feb 2026):**
- Customer interviews (5 pilots, 3 rounds each)
- Cost tracking (daily, target €0/month)
- Development logs (weekly reflections)
- Performance metrics (response time, uptime)

**Storage:**
- `data-collection/customer-interviews/` (anonymized transcripts)
- `data-collection/cost-tracking/` (Google Sheets exports)
- `data-collection/weekly-logs/` (markdown reflections)

---

## Quick Links

**Finnish Thesis:**
- [Opinnäytetyön suunnitelma (FI)](fi/OPINNAYTETYO_SUUNNITELMA_FI.md)

**English Reference:**
- [Thesis Outline (EN)](en/THESIS_OUTLINE.md)
- [Research Framework (EN)](en/RESEARCH_FRAMEWORK.md)

**Related Documents:**
- [Weekly Reports](/docs/Reports/) (EN + FI)
- [Roadmaps](/docs/roadmaps/) (MVP, Alpha, V1)
- [Sales Pipeline Agents](/CloudAgents/dws-team/SALES_PIPELINE_AGENTS.md)

---

**Last Updated:** December 3, 2025
**Status:** Thesis outline complete, awaiting Metropolia supervisor meeting
**Next Steps:**
1. Meet with Metropolia supervisor (finalize scope)
2. Begin MVP implementation (December 2025)
3. Start data collection (customer interviews, cost tracking)
