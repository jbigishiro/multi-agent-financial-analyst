from fastapi.testclient import TestClient
from unittest.mock import patch

from app import app


client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_analyze():

    fake_result = {
        "company": "NVIDIA",
        "research": "Research result",
        "finance": "Financial result",
        "risk": "Risk result",
        "report": "Final NVIDIA report",
        "next": "end",
    }

    with patch(
        "services.analysis.graph.invoke",
        return_value=fake_result
    ):

        response = client.post(
            "/analyze",
            json={
                "company": "NVIDIA"
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert data["company"] == "NVIDIA"
    assert data["report"] == "Final NVIDIA report"
    assert data["request_id"]


def test_empty_company():

    response = client.post(
        "/analyze",
        json={
            "company": ""
        }
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Company name cannot be empty."
    }