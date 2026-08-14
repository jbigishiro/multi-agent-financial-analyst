from config.llm import get_llm

def create_writer_agent():
    llm = get_llm()
    return llm