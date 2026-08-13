from graph.workflow import graph


initial_state = {
    "company": "NVIDIA",
    "research": "",
    "finance": "",
    "risk": "",
    "report": "",
}

result = graph.invoke(initial_state)

print("\nFinal State:")
print(result)