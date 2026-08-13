from agents.research import create_research_agent

agent = create_research_agent()
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "What are the latest developments "
                    "affecting NVIDIA?"
                ),
            }
        ]
    }
)

for message in result["messages"]:
    print("\n---")
    print(type(message).__name__)
    print(message)