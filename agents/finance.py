from config.llm import get_llm

def create_finance_agent():
    llm = get_llm()
    return llm