from langchain_core.retrievers import BaseRetriever

from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store
from rag.retriever import create_retriever


def create_financial_retriever(file_path: str,persist_directory: str,) -> BaseRetriever:
    """
    Build a retriever from an uploaded financial PDF.
    """
    documents = load_pdf(file_path)
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks,persist_directory=persist_directory,)

    return create_retriever(vector_store)