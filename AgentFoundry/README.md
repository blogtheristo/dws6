# AgentFoundry

**Agent Framework and Deployment Scripts**

This directory contains deployment scripts and frameworks for managing AI agents across different industries and use cases.

## Structure

```
AgentFoundry/
├── README.md                    # This file
├── Construction/                # Construction industry agents
│   └── create-SiteSense Agent.csv
└── [Future Industry Folders]/   # Additional industries as needed
```

## Purpose

AgentFoundry provides a structured approach to:
- **Agent Deployment**: Scripts and configurations for deploying AI agents
- **Phased Rollouts**: Gradual deployment strategies to ensure reliability
- **Industry-Specific Agents**: Organized by industry vertical
- **Deployment Tracking**: Clear phases and goals for each agent rollout

---

## Construction Industry

### SiteSense Agent

**Purpose**: AI-powered edge computing system for construction site monitoring, material optimization, and predictive logistics.

**Deployment Phases**:

| Phase | Name | Action | Goal |
|-------|------|--------|------|
| **Phase 1** | The "Silent" Pilot | Deploy 1 Agent (Camera + Edge Box) on a site | Train the AI. Let it "watch" the site and predict needs without ordering trucks. Compare its predictions to actuals to calibrate accuracy. |
| **Phase 2** | The "Advisor" | Activate the dashboard for Site Managers | Human-in-the-loop. The Agent sends alerts/suggestions to the manager, who manually confirms the truck orders. |
| **Phase 3** | Autonomous Mode | Full integration with Supplier APIs | Just-in-Time. The Agent manages the delivery schedule autonomously within set parameters (e.g., +/- 30 min adjustments). |

### Key Features

- **Real-time Monitoring**: <100ms latency edge inference
- **Computer Vision**: YOLO-based material detection and volumetric estimation
- **IoT Integration**: Sensor data aggregation from site equipment
- **Weather Intelligence**: API integration for predictive planning
- **Predictive Logistics**: Demand prediction engine with supplier integration

### Technical Stack

- **Edge Hardware**: NVIDIA Jetson devices
- **Inference**: Groq LPU for low-latency AI processing
- **Cloud**: Google Cloud Run for orchestration
- **IoT**: AWS IoT Greengrass for edge device management
- **APIs**: Weather APIs, supplier logistics APIs

---

## Usage

### Adding a New Agent

1. Create a new industry folder (e.g., `Manufacturing/`, `Energy/`)
2. Add deployment scripts following the naming convention: `create-[AgentName].csv` or `create-[AgentName].sh`
3. Document the agent in this README

### Deployment Script Format

Deployment scripts should follow a phased approach:
- **Phase 1**: Silent pilot / training phase
- **Phase 2**: Human-in-the-loop / advisory phase  
- **Phase 3**: Autonomous / production phase

---

## Related Documentation

- **SiteSense Agent Details**: See `dws10.com/construction/index.html` for full product description
- **Architecture**: See `ARCHITECTURE_SUMMARY.md` for system architecture
- **Agent Framework**: See `lifetime-agent-foundry/AGENT_FOUNDRY.md` for development framework

---

**Last Updated**: January 2026

