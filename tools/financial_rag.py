from langchain_core.tools import tool
from rag.retriever import create_retriever

def create_financial_rag_tool(retriever):

    @tool
    def search_financial_documents(query: str) -> str:
        """Search the company's financial documents for relevant information."""

        documents = retriever.invoke(query)
        if not documents:
            return "No relevant financial information was found."

        results = []
        for document in documents:
            results.append(document.page_content)

        return "\n\n".join(results)

    return search_financial_documents