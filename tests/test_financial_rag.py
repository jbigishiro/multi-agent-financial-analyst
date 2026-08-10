from langchain_core.documents import Document
from tools.financial_rag import create_financial_rag_tool

class FakeRetriever:

    def invoke(self, query):
        return [
            Document(
                page_content="NVIDIA reported strong revenue growth.",
                metadata={"source": "test"},
            ),
            Document(
                page_content="NVIDIA develops GPUs for accelerated computing.",
                metadata={"source": "test"},
            ),
        ]

def test_financial_rag_tool():
    retriever = FakeRetriever()
    tool = create_financial_rag_tool(retriever)
    result = tool.invoke(
        {"query": "What does NVIDIA do?"}
    )

    assert "revenue growth" in result
    assert "GPUs" in result