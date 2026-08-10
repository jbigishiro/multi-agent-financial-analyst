from langchain_core.tools import tool
from tavily import TavilyClient
from config.settings import settings

@tool
def search_web(query: str) -> str:
    """
    Search the web for current information.
    Use this tool when up-to-date or external information
    is required.
    """
    if not query.strip():
            raise ValueError("Search query cannot be empty.")
    
    client = TavilyClient(api_key=settings.tavily_api_key)
    response = client.search(query=query, max_results=5,)

    results = []

    for item in response.get("results", []):
        title = item.get("title", "")
        url = item.get("url", "")
        content = item.get("content", "")

        results.append(
            f"Title: {title}\n"
            f"URL: {url}\n"
            f"Content: {content}"
        )

    return "\n\n".join(results)