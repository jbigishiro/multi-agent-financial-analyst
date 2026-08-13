from typing import Literal
from pydantic import BaseModel


class Route(BaseModel):
    next: Literal[
        "research",
        "finance",
        "risk",
        "writer",
        "end",
    ]