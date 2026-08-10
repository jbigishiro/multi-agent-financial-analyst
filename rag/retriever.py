from langchain_core.retrievers import BaseRetriever

def create_retriever(vector_store) -> BaseRetriever:
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )