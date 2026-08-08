from tools.calculator import (
    calculate_revenue_growth,
    calculate_profit_margin,
    calculate_debt_to_equity,
)


growth = calculate_revenue_growth.invoke({
    "current_revenue": 100,
    "previous_revenue": 80,
})

margin = calculate_profit_margin.invoke({
    "net_income": 20,
    "revenue": 100,
})

debt_to_equity = calculate_debt_to_equity.invoke({
    "total_debt": 50,
    "shareholder_equity": 100,
})


print("Revenue growth:", growth)
print("Profit margin:", margin)
print("Debt-to-equity:", debt_to_equity)