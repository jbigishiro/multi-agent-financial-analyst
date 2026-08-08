from config.llm import get_llm
from config.logging import logger


def main():

    logger.info("Starting LLM test")

    llm = get_llm()

    logger.info("LLM client created")

    response = llm.invoke(
        "Explain machine learning in one sentence."
    )

    logger.info("LLM response received")

    print("\nResponse:")
    print(response.content)


if __name__ == "__main__":
    main()