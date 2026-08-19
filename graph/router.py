from typing import Literal
from pydantic import BaseModel

class Route(BaseModel):
    next: Literal[ "analysis","writer","end",]