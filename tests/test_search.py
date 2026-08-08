from tools.search import search_web


def test_search_web():
    result = search_web.invoke({
        "query": "NVIDIA latest earnings",
    })

    print(result)

    assert result