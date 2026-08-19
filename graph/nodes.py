import time
from tools.search import search_web
from tools.agent_tools import execute_tool_calls
from rag.pipeline import create_financial_retriever
from graph.state import FinancialAnalysisState
from agents.research import create_research_agent
from agents.finance import create_finance_agent
from agents.risk import create_risk_agent
from agents.writer import create_writer_agent
from agents.supervisor import create_supervisor



# Response Validation

def validate_response(response, agent_name):
    """
    Validate that an LLM agent returned usable content.
    """

    if response is None:
        raise ValueError(
            f"{agent_name} returned no response."
        )

    if not response.content:
        raise ValueError(
            f"{agent_name} returned empty content."
        )

    return response.content

# Basic Agent Retry

def invoke_with_retry(agent, prompt, retries=1,):
    """
    Invoke an agent with a limited number of retries.
    """
    for attempt in range(retries + 1):
        try:
            return agent.invoke(prompt)
        except Exception as e:
            if attempt == retries:
                raise
            print(f"Agent failed: {e}. Retrying ({attempt + 1}/{retries})...")

            time.sleep(2)


# Agent Initialization

research_agent = create_research_agent()
finance_agent = create_finance_agent()
risk_agent = create_risk_agent()
writer_agent = create_writer_agent()
supervisor = create_supervisor()

# Supervisor Node

def supervisor_node(state: FinancialAnalysisState):
    """
    Supervisor determines the next stage of the workflow.
    """
    result = supervisor.invoke(
        [
            (
                "system",
                """
                You are the supervisor of a financial analysis system.
                Your job is to determine the next stage.
                Choose one:
                - analysis: Run the Research, Finance, and Risk agents.
                - writer:Create the final financial report.
                - end:
                    Finish the workflow.
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

# Agent + Tool Execution

def invoke_agent_with_tools(agent, prompt, tools, retries=2, max_tool_iterations=3,):
    """
    Invoke an LLM agent and execute requested tools.
    max_tool_iterations prevents an agent from repeatedly
    calling the same tool forever.
    """
    messages = [("human", prompt)]
    tools_by_name = {tool.name: tool for tool in tools}

    for attempt in range(retries + 1):
        try:
            for iteration in range(max_tool_iterations):
                response = agent.invoke(messages)
                print(f"Agent response received. Tool calls: {len(response.tool_calls)}"
                )

                # No tool calls = final response
                if not response.tool_calls:
                    print( f"Final response received.  Tool calls: 0")
                    return response
                print(f"Agent requested tools: {[call['name'] for call in response.tool_calls]}")

                # Execute tools
                tool_messages = execute_tool_calls(response, tools_by_name,)
                messages.extend([response,*tool_messages,])
                print(f"Follow-up response received. Tool calls: {len(response.tool_calls)}")

            raise RuntimeError("Agent exceeded maximum, tool-call iterations.")

        except Exception as e:

            if attempt == retries:
                raise
            print(f"Agent tool execution failed: {e}")
            print(f"Retrying agent, ({attempt + 1}/{retries})...")

            time.sleep(2)

    raise RuntimeError(
        "Agent failed to produce a final response."
    )

# Start Analysis Node

def start_analysis_node(state: FinancialAnalysisState,):
    """
    Start the analysis phase.
    No state changes are required here.
    """
    return {}

# Research Node

def research_node(state: FinancialAnalysisState,):
    print("Research node running...")
    company = state["company"]
    try:

        response = invoke_agent_with_tools(
            research_agent,
            f"""
            You are a financial researcher
            Research the company: {company}
            Focus on:
            - Recent developments
            - Company announcements
            - Industry trends
            - Competitors
            - Market developments
            Use the web search tool to find current information.
            Do not invent facts.
            Generate a summary report not more than 5000 characters
            """,
            tools=[search_web],
            retries=2,
            max_tool_iterations=3,
        )

        content = validate_response(response, "Research agent",)
        print(
            f"Research output length: {len(content)} characters")
        return {"research": content}

    except Exception as e:
        print(f"Research agent failed: {e}")
        return {"research": (f"Research unavailable: {e}")}

# Finance Node

def finance_node(state: FinancialAnalysisState,):
    print("Finance node running...")

    company = state["company"]
    document_path = state["document_path"]
    request_id = state["request_id"]

    # IMPORTANT:
    # Each request gets its own Chroma directory.
    persist_directory = (f"data/chroma/{request_id}")
    try:
        # Build retriever from uploaded PDF
        retriever = create_financial_retriever(file_path=document_path, persist_directory=persist_directory,)

        # Retrieve relevant financial information
        documents = retriever.invoke(
            f"""
            Find financial information about {company}.

            Focus on:

            - Revenue
            - Profitability
            - Cash flow
            - Major financial trends
            - Important financial risks
            """
        )

        if not documents:
            raise ValueError(
                "No relevant financial information found."
            )

        financial_context = "\n\n".join(
            document.page_content
            for document in documents
        )

        print(
            f"Financial context length: "
            f"{len(financial_context)} characters"
        )

        # Finance Agent Prompt
        prompt = f"""
        Analyze the financial information for {company}.
        Use ONLY the financial information provided below.
        Financial information:{financial_context}
        Focus on:
        - Revenue
        - Profitability
        - Cash flow
        - Major financial trends
        - Important financial risks
        Clearly distinguish facts from analysis.
        Do not invent information.
        """
        # Invoke Finance Agent
        response = invoke_with_retry( finance_agent, prompt, retries=1,)
        content = validate_response( response,"Finance agent",)
        print(f"Finance output length: {len(content)} characters")
        return {"finance": content}

    except Exception as e:
        print(f"Finance agent failed: {e}")
        return {"finance": ( f"Financial analysis unavailable: {e}")}

# Risk Node

def risk_node(state: FinancialAnalysisState,):
    print("Risk node running...")
    company = state["company"]
    prompt = f"""
    You are a financial risk analyst
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
    Do not invent facts.
    Generate a summary report not more than 5000 characters
    """
    try:

        response = invoke_agent_with_tools(risk_agent, prompt,tools=[search_web],retries=2,max_tool_iterations=3,)
        content = validate_response(response,"Risk agent",)
        print(f"Risk output length: {len(content)} characters")
        return {"risk": content}

    except Exception as e:
        print(f"Risk agent failed: {e}")
        return { "risk": (f"Risk analysis unavailable: {e}")}

# Writer Node

def writer_node(state: FinancialAnalysisState,):
    print("Writer node running...")
    company = state["company"]
    research = state["research"]
    finance = state["finance"]
    risk = state["risk"]
    print(f"Research length: {len(research)} characters")
    print(f"Finance length: {len(finance)} characters")
    print(f"Risk length: {len(risk)} characters")

    prompt = f"""
        Create a professional financial analysis report for {company}.
        Research: {research}
        Financial analysis: {finance}
        Risk analysis: {risk}
        Structure the report with:
        1. Executive Summary
        2. Company Research
        3. Financial Analysis
        4. Key Risks
        5. Overall Assessment
        Clearly distinguish facts from analysis.
        Do not invent information.
        The report should have less than 5000 characters
        """
    try:
        response = invoke_with_retry( writer_agent, prompt, retries=1,)
        content = validate_response(response, "Writer agent",)
        print(f"Writer output length: {len(content)} characters")
        return {"report": content}

    except Exception as e:
        print(f"Writer failed: {e}")
        raise

# Supervisor Router

def route_from_supervisor(state: FinancialAnalysisState,):
    """
    Return the Supervisor's routing decision.
    """
    return state["next"]

# Analysis Complete Node

def analysis_complete_node(state: FinancialAnalysisState,):
    print( "All analysis agents completed.")
    return {}