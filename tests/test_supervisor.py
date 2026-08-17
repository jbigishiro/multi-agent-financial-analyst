from agents.supervisor import create_supervisor


def test_supervisor():

    supervisor = create_supervisor()

    result = supervisor.invoke(
        [
            (
                "system",
                """
                You are the supervisor of a financial analysis system.

                Choose the next stage:

                - analysis: run the Research, Finance, and Risk agents
                - writer: create the final report
                - end: finish the workflow
                """
            ),
            (
                "human",
                "We need current NVIDIA news."
            ),
        ]
    )

    print(result)

    assert result.next in {
        "analysis",
        "writer",
        "end",
    }