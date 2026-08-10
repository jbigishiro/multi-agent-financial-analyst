from rag.embeddings import get_embeddings

def test_embedding_model():
    embeddings = get_embeddings()

    vector = embeddings.embed_query(
        "NVIDIA artificial intelligence"
    )
    assert vector
    assert len(vector) > 0