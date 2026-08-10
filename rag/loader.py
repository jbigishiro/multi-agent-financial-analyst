from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(file_path: str) -> list[Document]:
    """
    Load a PDF file and return its pages as LangChain Documents.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {file_path}"
        )
    if path.suffix.lower() != ".pdf":
        raise ValueError(
            f"Expected a PDF file, got: {path.suffix}"
        )
    loader = PyPDFLoader(str(path))
    documents = loader.load()
    return documents