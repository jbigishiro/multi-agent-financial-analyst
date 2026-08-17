from unittest.mock import patch

from services.analysis import run_analysis


def test_run_analysis():

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
    ) as mock_invoke:

        result = run_analysis(
            company="NVIDIA",
            request_id="test-request-123"
        )

    assert result["company"] == "NVIDIA"
    assert result["report"] == "Final NVIDIA report"

    mock_invoke.assert_called_once()

def test_run_analysis_empty_report():

    fake_result = {
        "company": "NVIDIA",
        "research": "",
        "finance": "",
        "risk": "",
        "report": "",
        "next": "end",
    }

    with patch(
        "services.analysis.graph.invoke",
        return_value=fake_result
    ):

        try:
            run_analysis(
                company="NVIDIA",
                request_id="test-request-456"
            )
            assert False

        except RuntimeError as e:
            assert str(e) == (
                "Analysis workflow returned an empty report."
            )