
from agents.base_agent import BaseAgent
from data.mock_data import KYC_DB

class ContextGatherer(BaseAgent):
    def __init__(self):
        super().__init__("Context Gatherer")

    def run(self, alert_data):
        subject_id = alert_data.get("subject_id")
        print(f"[{self.name}] Querying KYC Profile for {subject_id}...")
        
        profile = KYC_DB.get(subject_id)
        if not profile:
            return {"error": "KYC Profile not found"}
        
        return {"kyc_profile": profile}
