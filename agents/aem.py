
from agents.base_agent import BaseAgent

class ActionExecutionModule(BaseAgent):
    def __init__(self):
        super().__init__("AEM")

    def run(self, decision_data):
        print(f"[{self.name}] Received Decision: {decision_data}")
        
        recommendation = decision_data.get("recommendation", "").upper()
        alert_id = decision_data.get("alert_id")
        rationale = decision_data.get("rationale")

        if "RFI" in recommendation or "REQUEST_INFORMATION" in recommendation:
            print(f">>> Action Executed: RFI via Email. Drafted message for Customer: requesting Source of Funds.")
        
        elif "IVR" in recommendation:
            print(f">>> Action Executed: IVR Call Initiated. Script ID 3 used for simple verification. Awaiting Customer Response...")
            
        elif "ESCALATE" in recommendation or "SAR" in recommendation:
            print(f">>> Action Executed: SAR Preparer Module Activated. Case {alert_id} pre-populated and routed to Human Queue.")
            print(f"    Rationale: {rationale}")
            
        elif "CLOSE" in recommendation or "FALSE POSITIVE" in recommendation:
            print(f">>> Action Executed: Alert Closed as False Positive.")
            print(f"    Rationale: {rationale}")
            
        else:
            print(f">>> Action Executed: Unknown Action. Logging for review.")
