from agents.supervisor import create_supervisor


def test_supervisor():
    supervisor = create_supervisor()

    result = supervisor.invoke(
        [
            ("system", """
            You are the supervisor of a financial analysis system.

            Choose the next agent:
            research, finance, risk, writer, or end.
            """),
            ("human", "We need current NVIDIA news."),
        ]
    )

    print(result)

    assert result.next in {
        "research",
        "finance",
        "risk",
        "writer",
        "end",
    }