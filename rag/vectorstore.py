from langchain_chroma import Chroma
from rag.embeddings import get_embeddings

def create_vector_store(documents, persist_directory="data/chroma",):
    embeddings = get_embeddings()
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
    return vector_store