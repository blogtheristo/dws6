"""
Customer Onboarding Workflow
Multi-agent orchestration using LlamaStack

This workflow coordinates multiple agents to:
1. Welcome new customers
2. Assess site requirements
3. Calculate hardware costs & payback period
4. Provision edge devices
5. Create success plan
"""

import asyncio
import httpx
from typing import Dict, Any
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Service endpoints
CLAUDE_ROUTER_URL = "http://claude-agent-router:8083"
EDGE_SYNC_SERVICE_URL = "http://edge-sync-service:8081"


class AgentOrchestrator:
    """Orchestrates multi-agent workflows"""

    def __init__(self):
        self.client = httpx.AsyncClient(timeout=30.0)

    async def invoke_agent(
        self,
        agent_id: str,
        messages: list,
        max_tokens: int = 4000
    ) -> Dict[str, Any]:
        """Invoke an agent via Claude Router"""
        try:
            response = await self.client.post(
                f"{CLAUDE_ROUTER_URL}/v1/agents/{agent_id}/invoke",
                json={
                    "messages": messages,
                    "max_tokens": max_tokens
                }
            )
            response.raise_for_status()
            return response.json()

        except httpx.HTTPError as e:
            logger.error(f"Error invoking agent {agent_id}: {e}")
            raise

    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()


async def customer_onboarding_workflow(
    customer_data: Dict[str, Any],
    vertical: str
) -> Dict[str, Any]:
    """
    Main customer onboarding workflow

    Args:
        customer_data: {
            "customer_id": "cust_123",
            "company_name": "Acme Construction",
            "contract_acv": 24000,
            "site_address": "Helsinki, Finland",
            "site_size_sqm": 5000,
            "project_type": "residential",
            "device_count": 2,
            "csm_email": "jane@lifetime.fi"
        }
        vertical: "construction", "manufacturing", etc.

    Returns:
        {
            "status": "success" | "failed",
            "steps_completed": [...],
            "payback_period_months": 1.8,
            "site_profile_id": "site_456",
            "success_plan_url": "..."
        }
    """

    orchestrator = AgentOrchestrator()
    workflow_result = {
        "status": "in_progress",
        "steps_completed": [],
        "errors": [],
        "start_time": datetime.utcnow().isoformat()
    }

    try:
        # Step 1: Send welcome email (Customer Satisfaction Agent)
        logger.info("Step 1: Sending welcome email")
        welcome_response = await orchestrator.invoke_agent(
            agent_id=f"customersat-{vertical}-001",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    New customer onboarded. Send welcome email with these details:

                    Customer: {customer_data['company_name']}
                    Contract ACV: €{customer_data['contract_acv']}
                    Assigned CSM: {customer_data['csm_email']}
                    Vertical: {vertical.title()}

                    Include:
                    - Welcome message
                    - Next steps for setup
                    - CSM contact information
                    - 30-day success milestones
                    """
                }
            ]
        )

        workflow_result["steps_completed"].append({
            "step": "welcome_email",
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        })
        logger.info("✓ Welcome email sent")

        # Step 2: Create site profile (SiteSense Cloud Agent)
        logger.info("Step 2: Creating site profile")
        site_profile_response = await orchestrator.invoke_agent(
            agent_id=f"sitesense-cloud-{vertical}-001",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Create a site profile for new customer:

                    Site Address: {customer_data['site_address']}
                    Site Size: {customer_data['site_size_sqm']} sqm
                    Project Type: {customer_data['project_type']}
                    Required Devices: {customer_data['device_count']}

                    Generate:
                    - Site profile ID
                    - Recommended device placement
                    - Network configuration requirements
                    - IoT sensor types needed
                    """
                }
            ]
        )

        workflow_result["steps_completed"].append({
            "step": "site_profile",
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        })
        logger.info("✓ Site profile created")

        # Step 3: Calculate hardware costs and payback (Viability Agent)
        logger.info("Step 3: Calculating viability metrics")
        viability_response = await orchestrator.invoke_agent(
            agent_id=f"viability-{vertical}-001",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Calculate viability metrics for this customer:

                    Customer ID: {customer_data['customer_id']}
                    Annual Contract Value: €{customer_data['contract_acv']}
                    Device Count: {customer_data['device_count']}
                    Site Size: {customer_data['site_size_sqm']} sqm

                    Calculate:
                    - Total hardware cost
                    - Setup cost (hours × rate)
                    - Monthly gross profit
                    - Payback period in months
                    - Gross margin %
                    - Viability score (0-100)

                    Provide JSON output with calculation breakdown.
                    """
                }
            ]
        )

        # Extract payback period from response
        # (In production, parse the structured JSON output)
        workflow_result["viability_metrics"] = "calculated"
        workflow_result["steps_completed"].append({
            "step": "viability_calculation",
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        })
        logger.info("✓ Viability metrics calculated")

        # Decision point: Only proceed if payback <= 3 months
        # (In production, parse actual value from viability_response)
        assumed_payback_months = 1.8
        workflow_result["payback_period_months"] = assumed_payback_months

        if assumed_payback_months > 3:
            logger.warning(f"⚠ Payback period {assumed_payback_months} months exceeds threshold")
            workflow_result["status"] = "warning"
            workflow_result["warnings"] = [
                f"Payback period {assumed_payback_months} months exceeds 3-month threshold"
            ]
            # Don't proceed to edge deployment
        else:
            # Step 4: Provision edge devices (Edge Sync Service)
            logger.info("Step 4: Provisioning edge devices")

            # Call edge sync service to configure Jetson devices
            async with httpx.AsyncClient() as client:
                edge_response = await client.post(
                    f"{EDGE_SYNC_SERVICE_URL}/v1/devices/provision",
                    json={
                        "customer_id": customer_data["customer_id"],
                        "site_id": "site_456",  # From step 2
                        "device_count": customer_data["device_count"],
                        "model": "llama-3.1-8b-instruct-tensorrt",
                        "network_config": {
                            "wifi_ssid": "SiteNetwork",
                            "region": "eu-north-1"
                        }
                    }
                )
                edge_response.raise_for_status()

            workflow_result["steps_completed"].append({
                "step": "edge_device_provisioning",
                "status": "completed",
                "timestamp": datetime.utcnow().isoformat()
            })
            logger.info("✓ Edge devices provisioned")

        # Step 5: Create 30-day success plan (Customer Satisfaction Agent)
        logger.info("Step 5: Creating success plan")
        success_plan_response = await orchestrator.invoke_agent(
            agent_id=f"customersat-{vertical}-001",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Create a 30-day customer success plan for:

                    Customer: {customer_data['company_name']}
                    Vertical: {vertical.title()}
                    Expected Payback: {assumed_payback_months} months

                    Include:
                    - Week 1: Onboarding milestones
                    - Week 2: Training completion
                    - Week 3: First production deployment
                    - Week 4: Performance review & NPS survey

                    Generate:
                    - Milestone checklist
                    - Training schedule
                    - Success criteria
                    - NPS survey trigger date
                    """
                }
            ]
        )

        workflow_result["steps_completed"].append({
            "step": "success_plan",
            "status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        })
        logger.info("✓ Success plan created")

        # Mark workflow as complete
        workflow_result["status"] = "success"
        workflow_result["end_time"] = datetime.utcnow().isoformat()

        logger.info("🎉 Customer onboarding workflow completed successfully")
        return workflow_result

    except Exception as e:
        logger.error(f"❌ Workflow failed: {e}", exc_info=True)
        workflow_result["status"] = "failed"
        workflow_result["errors"].append(str(e))
        workflow_result["end_time"] = datetime.utcnow().isoformat()
        return workflow_result

    finally:
        await orchestrator.close()


# Example usage
async def main():
    """Example workflow execution"""

    customer_data = {
        "customer_id": "cust_demo_001",
        "company_name": "Demo Construction Ltd",
        "contract_acv": 24000,
        "site_address": "Helsinki, Finland",
        "site_size_sqm": 5000,
        "project_type": "residential",
        "device_count": 2,
        "csm_email": "demo@lifetime.fi"
    }

    result = await customer_onboarding_workflow(
        customer_data=customer_data,
        vertical="construction"
    )

    print("\n" + "="*60)
    print("CUSTOMER ONBOARDING WORKFLOW RESULT")
    print("="*60)
    print(f"Status: {result['status']}")
    print(f"Payback Period: {result.get('payback_period_months', 'N/A')} months")
    print(f"\nSteps Completed ({len(result['steps_completed'])}):")
    for step in result['steps_completed']:
        print(f"  ✓ {step['step']} - {step['timestamp']}")

    if result.get('errors'):
        print(f"\nErrors:")
        for error in result['errors']:
            print(f"  ✗ {error}")

    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
