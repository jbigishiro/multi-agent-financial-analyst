from agents.risk import create_risk_agent


def test_risk_agent():
    agent = create_risk_agent()

    response = agent.invoke(
        """
        Identify two important current risks for NVIDIA.
        Use the search tool if necessary.
        """
    )

    print(response)

    assert response is not None