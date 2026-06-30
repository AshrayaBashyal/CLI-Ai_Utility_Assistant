
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


CURRENT_TIME_TOOL = {
    "type": "function",
    "function": {
        "name": "current_time",
        "description": (
            "Return the current local time. "
            "Use this whenever the user asks for the current time."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

TOOLS = [
    CALCULATOR_TOOL,
    CURRENT_TIME_TOOL,
]