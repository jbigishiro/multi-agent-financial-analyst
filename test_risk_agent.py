from agents.risk import create_risk_agent


agent = create_risk_agent()

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Identify the most important current risks facing NVIDIA"
                ),
            }
        ]
    }
)

for message in result["messages"]:
    print("\n====================")
    print(type(message).__name__)
    print(message)