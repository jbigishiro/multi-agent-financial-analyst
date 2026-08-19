from graph.state import create_initial_state
from graph.workflow import graph


def run_analysis(company: str,request_id: str,document_path: str,):

    state = create_initial_state(company,document_path,request_id,)
    config = {"configurable": {"thread_id": request_id}}
    result = graph.invoke(state,config=config
    )

    if not result:
        raise RuntimeError(
            "Analysis workflow returned no result."
        )

    if not result.get("report"):
        raise RuntimeError(
            "Analysis workflow returned an empty report."
        )

    return result