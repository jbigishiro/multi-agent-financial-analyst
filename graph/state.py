from typing import TypedDict, Literal

class FinancialAnalysisState(TypedDict):
    company: str
    research: str
    finance: str
    risk: str
    report: str
    next: Literal["analysis", "writer", "end"]