from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split documents into smaller chunks for retrieval.
    """
    if not documents:
        raise ValueError("Documents cannot be empty.")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return splitter.split_documents(documents)