from config.llm import get_llm

def create_finance_agent(tools=None):
    llm = get_llm()
    #if tools:
        #return llm.bind_tools(tools)
    return llm