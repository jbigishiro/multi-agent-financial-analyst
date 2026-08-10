from langchain_core.documents import Document
from rag.retriever import create_retriever
from rag.vectorstore import create_vector_store

def test_create_retriever(tmp_path):
    documents = [
        Document(
            page_content="NVIDIA develops GPUs and accelerated computing platforms.",
            metadata={"source": "test"},
        ),
        Document(
            page_content="NVIDIA reported strong revenue growth.",
            metadata={"source": "test"},
        ),
        Document(
            page_content="NVIDIA is headquartered in Santa Clara, California.",
            metadata={"source": "test"},
        ),
    ]

    vector_store = create_vector_store(
        documents,
        persist_directory=str(tmp_path),
    )

    retriever = create_retriever(vector_store)

    assert retriever is not None