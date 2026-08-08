import pytest
from tools.calculator import (
    calculate_revenue_growth,
    calculate_profit_margin,
    calculate_debt_to_equity,
)

def test_revenue_growth():
    result = calculate_revenue_growth.invoke({
        "current_revenue": 100,
        "previous_revenue": 80,
    })
    assert result == 25.0

def test_revenue_decline():
    result = calculate_revenue_growth.invoke({
        "current_revenue": 80,
        "previous_revenue": 100,
    })
    assert result == -20.0

def test_zero_previous_revenue():
    with pytest.raises(ValueError):
        calculate_revenue_growth.invoke({
            "current_revenue": 100,
            "previous_revenue": 0,
        })

def test_profit_margin():
    result = calculate_profit_margin.invoke({
        "net_income": 20,
        "revenue": 100,
    })
    assert result == 20.0

def test_profit_margin_zero_revenue():
    with pytest.raises(ValueError):
        calculate_profit_margin.invoke({
            "net_income": 20,
            "revenue": 0,
        })

def test_debt_to_equity():
    result = calculate_debt_to_equity.invoke({
        "total_debt": 50,
        "shareholder_equity": 100,
    })
    assert result == 0.5

def test_debt_to_equity_zero_equity():
    with pytest.raises(ValueError):
        calculate_debt_to_equity.invoke({
            "total_debt": 50,
            "shareholder_equity": 0,
        })