WEATHER_TOOL = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": (
            "Get the current weather metrics for a specified city, "
            "including temperature, real feel condition, humidity, "
            "wind speed, and precipitation."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": (
                        "The name of the target city to look up "
                        "(e.g., 'Butwal', 'New York')."
                    ),
                }
            },
            "required": ["city"],
        },
    },
}