
import os
from agents.orchestrator import Orchestrator
from data.mock_data import ALERTS
import sys

def main():
    print("Agentic Alert Resolution System (AARS) Initializing...")
    
    # Check for API Key
    if not os.getenv("GEMINI_API_KEY"):
        print("ERROR: GEMINI_API_KEY is not set. Please set it in your environment or .env file.")
        # sys.exit(1) # Commented out to allow dry run if needed, but Adjudicator will fail.

    orchestrator = Orchestrator()

    # Run for all alerts
    for alert in ALERTS:
        orchestrator.run(alert["alert_id"])

if __name__ == "__main__":
    main()
