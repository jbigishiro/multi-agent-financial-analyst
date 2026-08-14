from graph.workflow import graph


def test_full_workflow():
    initial_state = {
        "company": "NVIDIA",
        "research": "",
        "finance": "",
        "risk": "",
        "report": "",
        "next": "",
    }

    config = {
        "configurable": {
            "thread_id": "test-nvidia"
        }
    }

    result = graph.invoke(
        initial_state,
        config=config
    )

    print("\n================ FINAL REPORT ================\n")
    print(result["report"])

    assert result["report"]