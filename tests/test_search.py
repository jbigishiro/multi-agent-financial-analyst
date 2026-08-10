import pytest
from tools.search import search_web

def test_search_web():
    result = search_web.invoke({
        "query": "NVIDIA latest earnings",
    })
    assert result

def test_empty_search_query():
    with pytest.raises(ValueError):
        search_web.invoke({
            "query": "",
        })