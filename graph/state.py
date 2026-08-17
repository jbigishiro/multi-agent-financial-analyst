from typing import TypedDict, Literal

class FinancialAnalysisState(TypedDict):
    company: str
    research: str
    finance: str
    risk: str
    report: str
    next: Literal["analysis", "writer", "end"]

def create_initial_state(company: str) -> FinancialAnalysisState:
    return {
        "company": company,
        "research": "",
        "finance": "",
        "risk": "",
        "report": "",
        "next": "",
    }