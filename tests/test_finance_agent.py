from agents.finance import create_finance_agent

def test_create_finance_agent():
    agent = create_finance_agent(tools=[])
    assert agent is not None