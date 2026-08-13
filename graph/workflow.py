from langgraph.graph import StateGraph, START, END

from graph.state import FinancialAnalysisState
from graph.nodes import (
    supervisor_node,
    research_node,
    finance_node,
    risk_node,
    route_from_supervisor,
)


builder = StateGraph(FinancialAnalysisState)

builder.add_node("supervisor", supervisor_node)
builder.add_node("research", research_node)
builder.add_node("finance", finance_node)
builder.add_node("risk", risk_node)

builder.add_edge(START, "supervisor")

builder.add_conditional_edges(
    "supervisor",
    route_from_supervisor,
    {
        "research": "research",
        "finance": "finance",
        "risk": "risk",
        "writer": END,
        "end": END,
    },
)

builder.add_edge("research", END)
builder.add_edge("finance", END)
builder.add_edge("risk", END)

graph = builder.compile()