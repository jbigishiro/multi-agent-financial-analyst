import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, START, END
from graph.state import FinancialAnalysisState
from graph.nodes import (
    supervisor_node,
    start_analysis_node,
    research_node,
    finance_node,
    risk_node,
    analysis_complete_node,
    writer_node,
    route_from_supervisor,
)

conn = sqlite3.connect(
    "data/checkpoints.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(conn)
builder = StateGraph(FinancialAnalysisState)

# Nodes
builder.add_node("supervisor", supervisor_node)
builder.add_node("analysis", start_analysis_node)
builder.add_node("research", research_node)
builder.add_node("finance", finance_node)
builder.add_node("risk", risk_node)
builder.add_node("analysis_complete",analysis_complete_node,)
builder.add_node("writer", writer_node)

# START
builder.add_edge(START,"supervisor",)

# Supervisor Routing
builder.add_conditional_edges(
    "supervisor",
    route_from_supervisor,
    {
        "analysis": "analysis",
        "writer": "writer",
        "end": END,
    },
)

# Fan-Out
builder.add_edge("analysis", "research",)
builder.add_edge("analysis", "finance",)
builder.add_edge("analysis", "risk",)

# Fan-In / Synchronization
builder.add_edge("research","analysis_complete",)
builder.add_edge("finance","analysis_complete",)
builder.add_edge("risk","analysis_complete",)

# Analysis Complete → Writer
builder.add_edge("analysis_complete","writer",)

# Writer → END
builder.add_edge("writer",END,)

# Compile
graph = builder.compile(
    checkpointer=checkpointer
)