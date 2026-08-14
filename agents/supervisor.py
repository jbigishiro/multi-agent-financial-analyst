from pydantic import BaseModel
from typing import Literal
from config.llm import get_llm
from graph.router import Route

class SupervisorDecision(BaseModel):
    next: Literal["analysis", "writer", "end"]

def create_supervisor():
    llm = get_llm()
    structured_llm = llm.with_structured_output( SupervisorDecision)
    return structured_llm