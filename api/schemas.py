from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    company: str

class AnalysisResponse(BaseModel):
    request_id: str
    company: str
    report: str