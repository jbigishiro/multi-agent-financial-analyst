from config.llm import get_llm
from graph.router import Route

SUPERVISOR_PROMPT = """
You are the supervisor of a financial analysis system.
Decide which agent should work next.
Available agents:
- research: current company information and news
- finance: financial statements and financial data
- risk: company-specific risks
- writer: create the final report
- end: finish the workflow

Choose the next step based on the current state.
"""

def create_supervisor():
    llm = get_llm()
    structured_llm = llm.with_structured_output(Route)
    return structured_llm