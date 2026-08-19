import shutil
from pathlib import Path
from graph.state import create_initial_state
from graph.workflow import graph

def run_analysis(company: str, request_id: str,document_path: str,):
    state = create_initial_state(company=company, document_path=document_path, request_id=request_id,)
    config = {"configurable": {"thread_id": request_id}}
    chroma_directory = (Path("data/chroma")/request_id)

    try:
        result = graph.invoke( state, config=config,)

        if not result:
            raise RuntimeError("Analysis workflow returned no result.")

        if not result.get("report"):
            raise RuntimeError("Analysis workflow returned an empty report.")

        return result

    finally:
        # Delete uploaded PDF
        document = Path(document_path)
        if document.exists():
            try:
                document.unlink()
                print( f"Deleted uploaded document: {document}")

            except Exception as e:
                print(f"Failed to delete document {document}: {e}")

        # Delete request-specific Chroma database
        if chroma_directory.exists():
            try:
                shutil.rmtree(chroma_directory)
                print( f"Deleted Chroma data: {chroma_directory}")

            except Exception as e:
                print(
                    f"Failed to delete Chroma data {chroma_directory}: {e}")