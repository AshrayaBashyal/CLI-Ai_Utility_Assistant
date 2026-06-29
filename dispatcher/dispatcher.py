from tools.calculator import calculator


TOOL_REGISTRY = {
    "calculator": calculator,
}


def dispatch(tool_name: str, arguments: dict) -> dict:
    """
    Execute the requested tool with the provided arguments.
    """

    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        return {
            "success": False,
            "error": {
                "message": f"Unknown tool: {tool_name}"
            }
        }

    try:
        return tool(**arguments)

    except TypeError as e:
        return {
            "success": False,
            "error": {
                "message": f"Invalid arguments: {str(e)}"
            }
        }