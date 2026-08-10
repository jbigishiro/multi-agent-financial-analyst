import pytest
from rag.loader import load_pdf


def test_load_pdf():
    documents = load_pdf(
        "documents/nvidia_annual_report.pdf"
    )

    assert documents
    assert len(documents) > 0

def test_missing_pdf():
    with pytest.raises(FileNotFoundError):
        load_pdf("documents/does_not_exist.pdf")

def test_invalid_file_type():
    with pytest.raises(ValueError):
        load_pdf("documents/report.txt")