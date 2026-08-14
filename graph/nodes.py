import time
from graph.state import FinancialAnalysisState
from agents.research import create_research_agent
from agents.finance import create_finance_agent
from agents.risk import create_risk_agent
from agents.writer import create_writer_agent
from agents.supervisor import create_supervisor

def validate_response(response, agent_name):
    if response is None:
        raise ValueError(f"{agent_name} returned no response.")

    if not response.content:
        raise ValueError(f"{agent_name} returned empty content.")

    return response.content

def invoke_with_retry(agent, prompt, retries=2, timeout=60):
    for attempt in range(retries + 1):
        try:
            return agent.invoke(
                prompt,
                timeout=timeout
            )

        except Exception as e:
            if attempt == retries:
                raise

            print(
                f"Agent failed. "
                f"Retrying ({attempt + 1}/{retries})..."
            )

            time.sleep(2)
# Agents
research_agent = create_research_agent()
finance_agent = create_finance_agent()
risk_agent = create_risk_agent()
writer_agent = create_writer_agent()
supervisor = create_supervisor()

# Supervisor Node
def supervisor_node(state: FinancialAnalysisState):
    result = supervisor.invoke(
        [
            (
                "system",
                """
                You are the supervisor of a financial analysis system.
                Your job is to determine the next stage.
                Choose:
                - analysis: run the Research, Finance, and Risk agents
                - writer: create the final report
                - end: finish the workflow
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

# Start Analysis Node
def start_analysis_node(state: FinancialAnalysisState):
    return {}

# Research Node
def research_node(state: FinancialAnalysisState):
    print("Research node running...")
    company = state["company"]
    try:
        response = invoke_with_retry(
            research_agent,
            f"""
            Research the company: {company}

            Focus on:
            - recent developments
            - company announcements
            - industry trends
            - competitors
            - market developments

            Do not invent facts.
            """
        )

        content = validate_response(response, "Research agent")

        return { "research": content}

    except Exception as e:
        print(f"Research agent failed: {e}")
        return { "research": f"Research unavailable: {e}"}

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
    try:
       
        response = invoke_with_retry(finance_agent,prompt)
        content = validate_response(response, "Finance agent")

        return {"finance": content}
    
    except Exception as e:
        print(f"Finance agent failed: {e}")
        return { "finance": f"Financial analysis unavailable: {e}"}

# Risk Node
def risk_node(state: FinancialAnalysisState):
    print("Risk node running...")
    company = state["company"]
    prompt = f"""
                Identify the most important current risks for {company}.
                Focus on:
                - Business risks
                - Competitive risks
                - Regulatory risks
                - Technology risks
                - Market risks
                - Recent developments
                Use current information from the search tool.
                Be specific and avoid generic risks.
                """
    try:
        response = invoke_with_retry(
            risk_agent,
            prompt
        )
        content = validate_response(response, "Risk agent")

        return {
    "risk": content
}
    except  Exception as e:
        print(f"Risk agent failed: {e}")
        return {"risk": f"Risk analysis unavailable: {e}"} 

# Writer Node
def writer_node(state: FinancialAnalysisState):
    print("Writer node running...")

    company = state["company"]
    prompt = f"""
            Create a professional financial analysis report for {company}.
    
            Research: {state["research"]}
            Financial analysis: {state["finance"]}
            Risk analysis: {state["risk"]}
    
            Structure the report with:
            1. Executive Summary
            2. Company Research
            3. Financial Analysis
            4. Key Risks
            5. Overall Assessment
    
            Clearly distinguish facts from analysis.
            Do not invent information.
            """
    try:
        
        response = invoke_with_retry(writer_agent,prompt)

        content = validate_response(response, "Writer agent")

        return {"report": content}
    
    except Exception as e:
        print(f"Writer failed: {e}")
        return {"report": f"Report generation failed: {e}"}

# Router
def route_from_supervisor(state: FinancialAnalysisState):
    """
    Return the Supervisor's routing decision.
    """
    return state["next"]

# Analysis Complete Node
def analysis_complete_node(state: FinancialAnalysisState):
    print("All analysis agents completed.")
    return {}