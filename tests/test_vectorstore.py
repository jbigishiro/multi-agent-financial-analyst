from langchain_core.documents import Document
from rag.vectorstore import create_vector_store

def test_create_vector_store():
    documents = [
        Document(
            page_content=(
                "NVIDIA develops GPUs and accelerated "
                "computing platforms."
            ),
            metadata={"source": "test"},
        ),
        Document(
            page_content=(
                "NVIDIA operates in the artificial "
                "intelligence computing market."
            ),
            metadata={"source": "test"},
        ),
    ]
    
    vector_store = create_vector_store(documents)
    assert vector_store is not None