
from agents.base_agent import BaseAgent
from data.mock_data import TRANSACTION_DB

class Investigator(BaseAgent):
    def __init__(self):
        super().__init__("Investigator")

    def run(self, alert_data):
        subject_id = alert_data.get("subject_id")
        print(f"[{self.name}] Querying Transaction History for {subject_id}...")
        
        history = TRANSACTION_DB.get(subject_id)
        if not history:
            return {"error": "No transaction history found"}
        
        # In a real system, this would do more complex analysis.
        # Here we just pass the mock findings.
        return {"transaction_history": history}
