from graph.workflow import graph


def test_workflow_memory():

    config = {
        "configurable": {
            "thread_id": "memory-test"
        }
    }

    state = {
        "company": "NVIDIA",
        "research": "",
        "finance": "",
        "risk": "",
        "report": "",
        "next": "",
    }

    result = graph.invoke(
        state,
        config=config
    )

    saved_state = graph.get_state(config)

    print("\nSaved state:")
    print(saved_state.values)

    assert saved_state.values["company"] == "NVIDIA"
    assert saved_state.values["report"]