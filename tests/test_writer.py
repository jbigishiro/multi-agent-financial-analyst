from agents.writer import create_writer_agent


def test_writer():
    writer = create_writer_agent()

    response = writer.invoke(
        """
        Write a short financial analysis of NVIDIA.

        Research:
        NVIDIA develops GPUs and accelerated computing platforms.

        Finance:
        NVIDIA has experienced significant revenue growth.

        Risks:
        NVIDIA faces competition and regulatory risks.
        """
    )

    print(response.content)

    assert response.content