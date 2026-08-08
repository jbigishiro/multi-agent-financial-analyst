from langchain_core.tools import tool

@tool
def calculate_revenue_growth(current_revenue: float, previous_revenue: float,) -> float:
    """
    Calculate revenue growth as a percentage.
    Formula: ((current_revenue - previous_revenue) / previous_revenue) * 100
    """
    if previous_revenue == 0:
        raise ValueError("Previous revenue cannot be zero.")

    return ((current_revenue - previous_revenue)/ previous_revenue) * 100

@tool
def calculate_profit_margin(net_income: float, revenue: float,) -> float:
    """
    Calculate net profit margin as a percentage.
    Formula: (net_income / revenue) * 100
    """
    if revenue == 0:
        raise ValueError("Revenue cannot be zero.")

    return (net_income / revenue) * 100

@tool
def calculate_debt_to_equity(total_debt: float, shareholder_equity: float,) -> float:
    """
    Calculate the debt-to-equity ratio.
    Formula: total_debt / shareholder_equity
    """
    if shareholder_equity == 0:
        raise ValueError(
            "Shareholder equity cannot be zero.")

    return total_debt / shareholder_equity