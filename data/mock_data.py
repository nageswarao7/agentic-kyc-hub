
# 5 Alerts as per Assignment
ALERTS = [
    {
        "alert_id": "A-001",
        "scenario_code": "SCN-LAYER-01",
        "scenario_name": "Velocity Spike (Layering)",
        "subject_id": "CUST-001"
    },
    {
        "alert_id": "A-002",
        "scenario_code": "SCN-STRUCT-02",
        "scenario_name": "Below-Threshold Structuring",
        "subject_id": "CUST-002"
    },
    {
        "alert_id": "A-003",
        "scenario_code": "SCN-KYC-03",
        "scenario_name": "KYC Inconsistency",
        "subject_id": "CUST-003"
    },
    {
        "alert_id": "A-004",
        "scenario_code": "SCN-SANC-04",
        "scenario_name": "Sanctions List Hit",
        "subject_id": "CUST-004"
    },
    {
        "alert_id": "A-005",
        "scenario_code": "SCN-DORM-05",
        "scenario_name": "Dormant Account Activation",
        "subject_id": "CUST-005"
    }
]

# Mock KYC Profile Database
KYC_DB = {
    "CUST-001": {
        "name": "John Doe",
        "risk_rating": "Medium",
        "occupation": "Software Engineer",
        "employer": "Tech Corp",
        "income": 120000,
        "segment": "Retail",
        "age": 35
    },
    "CUST-002": {
        "name": "Jane Smith",
        "risk_rating": "High",
        "occupation": "Small Business Owner",
        "employer": "Smith Retail",
        "income": 80000,
        "segment": "SMB",
        "age": 45
    },
    "CUST-003": {
        "name": "Student A",
        "risk_rating": "Low",
        "occupation": "Student",
        "employer": "University",
        "income": 0,
        "segment": "Retail",
        "age": 20
    },
    "CUST-004": {
        "name": "Robert Badguy",
        "risk_rating": "High",
        "occupation": "Unknown",
        "employer": "Self",
        "income": 500000,
        "segment": "Retail",
        "age": 50
    },
    "CUST-005": {
        "name": "Grandma Old",
        "risk_rating": "Low",
        "occupation": "Retired",
        "employer": "N/A",
        "income": 20000,
        "segment": "Retail",
        "age": 80,
        "account_status_prev": "Dormant"
    }
}

# Mock Transaction History Database
# Simplified for the assignment needs
TRANSACTION_DB = {
    "CUST-001": {
        "recent_history": "5 transactions > $5000 in last 48 hours. Large inbound credit 2 hours prior.",
        "historical_velocity": "Low",
        "business_cycle_match": False
    },
    "CUST-002": {
        "recent_history": "3 cash deposits in 7 days: $9100, $9500, $9800.",
        "linked_accounts_aggregate": 28400, # > 28k
        "geo_diversity": True,
        "business_receipts_match": False
    },
    "CUST-003": {
        "recent_history": "$20,000 wire to 'Precious Metals Trading' MCC.",
        "historical_patterns": "Usually small coffee shop purchases."
    },
    "CUST-004": {
        "recent_history": "Transaction with counterparty 'Osama B. Laden' (80% match).",
        "counterparty_jurisdiction": "High Risk",
        "sanctions_match_true": True
    },
    "CUST-005": {
        "recent_history": "Inbound wire $15,000. Immediate large ATM withdrawal.",
        "last_activity_days": 400
    }
}

# SOP Rules (Simulated Knowledge Base)
SOP_RULES = {
    "A-001": "IF lookback no prior high velocity THEN ESCALATE (SAR). IF known business cycle THEN CLOSE (False Positive).",
    "A-002": "IF linked accounts aggregate > $28k THEN ESCALATE (SAR). IF deposits geographically diverse AND legitimate business receipts THEN RFI.",
    "A-003": "IF occupation == 'Jeweler'/'Trader' THEN CLOSE (False Positive). IF profile == 'Teacher'/'Student' THEN ESCALATE (SAR).",
    "A-004": "IF true match OR high-risk jurisdiction THEN ESCALATE (Block/SAR). IF false positive (common name) THEN CLOSE.",
    "A-005": "IF KYC Risk is Low AND RFI tool available THEN RFI. IF KYC Risk is High AND withdrawal is international/suspicious THEN ESCALATE (SAR)."
}
