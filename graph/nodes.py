from graph.state import FinancialAnalysisState
from agents.research import create_research_agent
from agents.finance import create_finance_agent
from agents.supervisor import create_supervisor

# Agents
research_agent = create_research_agent()
finance_agent = create_finance_agent()
supervisor = create_supervisor()

# Supervisor Node

def supervisor_node(state: FinancialAnalysisState):
    """
    Decide which agent should run next.
    """
    result = supervisor.invoke(
        [
            (
                "system",
                """
                You are the supervisor of a financial analysis system.
                Choose the next agent:
                - research: current company information and news
                - finance: financial statements and financial data
                - risk: company-specific risks
                - writer: create the final report
                - end: finish the workflow

                Choose the most appropriate next step.
                """,
            ),
            (
                "human",
                f"Analyze company: {state['company']}",
            ),
        ]
    )

    return {
        "next": result.next
    }

# Research Node

def research_node(state: FinancialAnalysisState):
    """
    Run the Research Agent.
    """
    print("Research node running...")

    result = research_agent.invoke(
        { "messages": [
                (
                    "user",
                    f"Research the company {state['company']}."
                )
            ]
        }
    )

    return {
        "research": result["messages"][-1].content
    }

# Finance Node
def finance_node(state: FinancialAnalysisState):
    print("Finance node running...")

    company = state["company"]

    prompt = f"""
    Analyze the financial information for {company}.
    Focus on:
    - Revenue
    - Profitability
    - Cash flow
    - Major financial trends
    - Important financial risks

    Use only the provided financial context.
    """
    response = finance_agent.invoke(prompt)
    return {"finance": response.content}

# Risk Node
def risk_node(state: FinancialAnalysisState):
    """
    Placeholder for the Risk Agent.
    We will implement the real Risk Agent later.
    """
    print("Risk node running...")
    return {
        "risk": "Risk analysis completed."
    }

# Router
def route_from_supervisor(state: FinancialAnalysisState):
    """
    Return the Supervisor's routing decision.
    """
    return state["next"]