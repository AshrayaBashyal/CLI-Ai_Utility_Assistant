#  it seems - Groq's hardware parser is broken for this tool.

CURRENT_TIME_TOOL = {
    "type": "function",
    "function": {
        "name": "current_time",
        "description": "Return the current local time. Use this whenever the user asks for the current time.",
        "parameters": {
            "type": "object",
            "properties": {
                "format": {
                    "type": "string",
                    "description": "Optional format preference (e.g., '12h', '24h'). Defaults to 12-hour AM/PM format."
                }
            },
            "required": []  # Keeping this empty means 'format' is completely optional
        }
    }
}
