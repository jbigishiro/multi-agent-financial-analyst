from typing import TypedDict, Literal

class FinancialAnalysisState(TypedDict):
    company: str
    document_path: str
    request_id: str
    research: str
    finance: str
    risk: str
    report: str
    next: Literal["analysis", "writer", "end"]

def create_initial_state(company: str,document_path: str,request_id: str,):
    return {
        "company": company,
        "document_path": document_path,
        "request_id": request_id,
        "research": "",
        "finance": "",
        "risk": "",
        "report": "",
        "next": "",
    }