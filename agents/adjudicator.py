
import os
import json
from agents.base_agent import BaseAgent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class Resolution(BaseModel):
    recommendation: str = Field(description="The final decision: 'ESCALATE (SAR)', 'CLOSE (False Positive)', 'RFI', etc.")
    rationale: str = Field(description="The reasoning behind the decision, citing specific SOP rules and data points.")
    confidence: str = Field(description="Confidence level (High/Medium/Low)")

class Adjudicator(BaseAgent):
    def __init__(self):
        super().__init__("Adjudicator")
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("WARNING: GEMINI_API_KEY not found in environment variables.")
        
        # Initialize Gemini
        # Ensure that google-generativeai is installed and key is valid
        if api_key:
            self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        else:
            self.llm = None

        self.parser = JsonOutputParser(pydantic_object=Resolution)

        self.prompt = PromptTemplate(
            template="""You are an expert AML (Anti-Money Laundering) Adjudicator Agent.
            Your job is to analyze a banking alert based on the provided data and Standard Operating Procedures (SOP).
            
            Alert Information:
            {alert_info}
            
            Transaction History:
            {transaction_history}
            
            KYC Profile:
            {kyc_profile}
            
            SOP Rules:
            {sop_rules}
            
            Instructions:
            1. Analyze the alert scenario against the Transaction History and KYC Profile.
            2. Apply the relevant SOP Rule for this Alert ID.
            3. Determine the resolution (Escalate, Close, RFI, etc.).
            4. Provide a clear rationale.
            
            Format your response as a JSON object with the following keys:
            - recommendation: The final decision.
            - rationale: The reasoning.
            - confidence: High/Medium/Low.
            
            {format_instructions}
            """,
            input_variables=["alert_info", "transaction_history", "kyc_profile", "sop_rules"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )
        
        if self.llm:
            self.chain = self.prompt | self.llm | self.parser
        else:
            self.chain = None

    def run(self, context_data):
        print(f"[{self.name}] Analyzing findings...")
        
        if not self.chain:
            return {
                "recommendation": "ERROR", 
                "rationale": "Missing Gemini API Key. Cannot perform reasoning.", 
                "confidence": "Low",
                "alert_id": context_data.get("alert", {}).get("alert_id")
            }

        try:
            result = self.chain.invoke({
                "alert_info": context_data.get("alert"),
                "transaction_history": context_data.get("transaction_history"),
                "kyc_profile": context_data.get("kyc_profile"),
                "sop_rules": context_data.get("sop_rule")
            })
            # Add alert_id back to result for AEM
            result["alert_id"] = context_data.get("alert", {}).get("alert_id")
            return result
        except Exception as e:
            print(f"[{self.name}] Error during reasoning: {e}")
            return {
                "recommendation": "ERROR", 
                "rationale": f"LLM Processing Failed: {str(e)}", 
                "confidence": "Low",
                "alert_id": context_data.get("alert", {}).get("alert_id")
            }
