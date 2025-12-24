
from agents.base_agent import BaseAgent
from agents.investigator import Investigator
from agents.context_gatherer import ContextGatherer
from agents.adjudicator import Adjudicator
from agents.aem import ActionExecutionModule
from data.mock_data import ALERTS, SOP_RULES

class Orchestrator(BaseAgent):
    def __init__(self):
        super().__init__("Orchestrator")
        self.investigator = Investigator()
        self.context_gatherer = ContextGatherer()
        self.adjudicator = Adjudicator()
        self.aem = ActionExecutionModule()

    def run(self, alert_id):
        print(f"\n{'='*50}")
        print(f"[{self.name}] Starting investigation for Alert ID: {alert_id}")
        
        # 1. Fetch Alert Data
        alert_data = next((a for a in ALERTS if a["alert_id"] == alert_id), None)
        if not alert_data:
            print(f"[{self.name}] Alert {alert_id} not found.")
            return

        print(f"[{self.name}] Scenario: {alert_data['scenario_name']}")

        # 2. Gather Evidence (Spokes)
        # In a more complex system, we would route based on scenario. created
        # Here we gather all available context.
        txn_history = self.investigator.run(alert_data)
        kyc_profile = self.context_gatherer.run(alert_data)

        # 3. Prepare Context for Adjudicator
        sop_rule = SOP_RULES.get(alert_id, "No SOP found")
        
        context = {
            "alert": alert_data,
            "transaction_history": txn_history,
            "kyc_profile": kyc_profile,
            "sop_rule": sop_rule
        }

        # 4. Adjudicate
        decision = self.adjudicator.run(context)
        
        # 5. Execute Action
        self.aem.run(decision)
        print(f"{'='*50}\n")
