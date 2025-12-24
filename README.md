# Agentic Alert Resolution System (AARS)

## Overview
This project implements a simplified **Agentic Alert Resolution System (AARS)** as per the assignment requirements. It is designed to automatically investigate and resolve banking transaction monitoring alerts using a **Hub and Spoke** multi-agent architecture.

The core reasoning engine is powered by **LangChain** and **Google Gemini** (LLM), enabling dynamic and reasoning-based resolution of complex alert scenarios (SOPs).

## Architecture

The system follows a modular Hub and Spoke pattern:

- **Orchestrator (Hub)**: The central controller that routes alerts and manages the investigation lifecycle.
- **Spoke Agents**:
  - **Investigator**: Simulates querying the Transaction History database.
  - **Context Gatherer**: Simulates querying the KYC (Know Your Customer) Profile database.
  - **Adjudicator**: The "Brain" of the operation. It uses an LLM (Gemini Pro via LangChain) to reason over the gathered evidence and apply the specific Standard Operating Procedure (SOP) rules to reach a decision.
- **Action Execution Module (AEM)**: Executes the final resolution (e.g., filing a SAR, initiating a customer RFI, or closing as False Positive).

## Features

- **5 Distinct Scenarios**: Handles Velocity Spikes, Structuring, KYC Inconsistencies, Sanctions Hits, and Dormant Account Activation.
- **LLM Reasoning**: Uses Generative AI to interpret rules and text, rather than hard-coded `if/else` statements for the final decision.
- **Auditable Output**: Provides clear console logs simulating real-world actions (IVR, Email RFI, SAR filings).

## Project Structure

```
KYC_Hub/
├── agents/                 # Agent Implementations
│   ├── base_agent.py       # Abstract Base Class
│   ├── orchestrator.py     # Hub Agent
│   ├── investigator.py     # Transaction History Spoke
│   ├── context_gatherer.py # KYC Spoke
│   ├── adjudicator.py      # Reasoning Spoke (LangChain + Gemini)
│   └── aem.py              # Action Execution Module
├── data/
│   └── mock_data.py        # Mock Databases and SOP Rules
├── main.py                 # Application Entry Point
├── requirements.txt        # Python Dependencies
├── .env.example            # Environment Variable Template
├── .gitignore              # Git Ignore File
└── README.md               # project Documentation
```

## Setup & Installation

1.  **Prerequisites**: Python 3.9+ installed.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Environment Configuration**:
    - Rename `.env.example` to `.env` (or set the variable directly).
    - Add your Google Gemini API Key:
      ```
      GEMINI_API_KEY=your_api_key_here
      ```

## Usage

To run the simulation for all 5 assignment alerts:

```bash
python main.py
```

## Evaluation Criteria Mapping

- **Agentic Architecture**: Implemented in `agents/orchestrator.py` delegating to specific agents in `agents/`.
- **Resolution Logic**: Controlled by `agents/adjudicator.py` using `data/mock_data.py` (SOPs).
- **Tool Integration**: `agents/aem.py` simulates the downstream tool actions based on the Adjudicator's structured JSON output.
