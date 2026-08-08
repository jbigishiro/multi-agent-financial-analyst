from tools.finance import get_company_info

def test_get_company_info():
    result = get_company_info.invoke({
        "ticker": "NVDA",
    })

    assert result
    assert "NVDA" in result