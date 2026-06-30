
CALCULATOR_TOOL = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": (
            "Evaluate a mathematical expression. "
            "Use this tool whenever the user asks for a calculation."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": (
                        "The mathematical expression to evaluate."
                    ),
                }
            },
            "required": ["expression"],
        },
    },
}


TOOLS = [CALCULATOR_TOOL]