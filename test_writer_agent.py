from agents.writer import create_writer_agent


agent = create_writer_agent()


research = """
NVIDIA continues to benefit from strong demand for
AI infrastructure and accelerated computing.
"""

finance = """
NVIDIA has experienced significant revenue growth
driven by demand for data-center GPUs.
"""

risk = """
Export restrictions and increasing competition in
AI accelerators represent important risks.
"""


prompt = f"""
Create a financial analysis of NVIDIA using the
following analyst findings.

RESEARCH FINDINGS:
{research}

FINANCE FINDINGS:
{finance}

RISK FINDINGS:
{risk}
"""


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    }
)

for message in result["messages"]:
    print("\n====================")
    print(type(message).__name__)
    print(message)