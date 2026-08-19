from langchain_core.messages import ToolMessage

def execute_tool_calls(response, tools_by_name):
    """
    Execute tool calls returned by an LLM.
    """
    tool_results = []

    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_call_id = tool_call["id"]
        tool = tools_by_name.get(tool_name)

        if tool is None:
            raise ValueError(f"Unknown tool requested: {tool_name}")

        result = tool.invoke(tool_args)
        tool_results.append(ToolMessage(content=result, tool_call_id=tool_call_id,))

    return tool_results