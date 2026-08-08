from langchain_core.tools import tool
import yfinance as yf

@tool
def get_company_info(ticker: str) -> str:
    """
    Retrieve basic company information for a stock ticker.
    """
    ticker = ticker.upper().strip()
    stock = yf.Ticker(ticker)
    info = stock.info
    company_name = info.get("longName", "Unknown")
    sector = info.get("sector", "Unknown")
    industry = info.get("industry", "Unknown")
    country = info.get("country", "Unknown")

    return (
        f"Company: {company_name}\n"
        f"Ticker: {ticker}\n"
        f"Sector: {sector}\n"
        f"Industry: {industry}\n"
        f"Country: {country}"
    )