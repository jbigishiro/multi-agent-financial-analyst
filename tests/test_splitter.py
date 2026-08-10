import pytest
from langchain_core.documents import Document
from rag.splitter import split_documents


def test_split_documents():
    documents = [
        Document(
            page_content="A " * 1000,
            metadata={"page": 1},
        )
    ]

    chunks = split_documents(documents)

    assert chunks
    assert len(chunks) > 1

    for chunk in chunks:
        assert chunk.metadata["page"] == 1