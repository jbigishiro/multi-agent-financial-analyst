from langchain.agents import create_agent
from config.llm import get_llm
from tools.search import search_web

RESEARCH_SYSTEM_PROMPT = """
    You are a financial research specialist.
    Your job is to research current external information
    about companies and industries.
    Use web search when current or external information
    is required.
    Focus on:
    - recent developments
    - company announcements
    - industry trends
    - competitors
    - market developments
    Do not invent facts.
    Base your answers on information returned by your tools.
    """

def create_research_agent():
    llm = get_llm()
    return create_agent(model=llm, tools=[search_web],system_prompt=RESEARCH_SYSTEM_PROMPT,)

