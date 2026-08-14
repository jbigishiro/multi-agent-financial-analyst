from config.llm import get_llm
from tools.search import search_web

def create_research_agent():
    llm = get_llm()
    return llm.bind_tools([search_web])

