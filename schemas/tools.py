
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


UNIT_CONVERTER_TOOL = {
    "type": "function",
    "function": {
        "name": "convert",
        "description": (
            "Converts measurements across different units for length, "
            "weight, volume, or temperature."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "number",
                    "description": "The numerical measurement value to convert."
                },
                "from_unit": {
                    "type": "string",
                    "enum": [
                        "mm", "cm", "m", "km", "in", "ft", "yd", "mi", 
                        "mg", "g", "kg", "oz", "lb", 
                        "ml", "l", "tsp", "tbsp", "fl_oz", "cup", "gal", 
                        "c", "f", "k"
                    ],
                    "description": "The unit abbreviation you are converting from."
                },
                "to_unit": {
                    "type": "string",
                    "enum": [
                        "mm", "cm", "m", "km", "in", "ft", "yd", "mi", 
                        "mg", "g", "kg", "oz", "lb", 
                        "ml", "l", "tsp", "tbsp", "fl_oz", "cup", "gal", 
                        "c", "f", "k"
                    ],
                    "description": "The unit abbreviation you want to convert into."
                }
            },
            "required": ["value", "from_unit", "to_unit"]
        }
    }
}


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

CURRENCY_CONVERTER_TOOL = {
    "type": "function",
    "function": {
        "name": "convert_currency",
        "description": "Converts currency amounts between dynamic fiat options using live central bank indices.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "The exact total numerical value of money to convert. Must be greater than 0."
                },
                "from_currency": {
                    "type": "string",
                    "description": "The standard 3-letter currency code to convert from (e.g., USD, EUR, GBP)."
                },
                "to_currency": {
                    "type": "string",
                    "description": "The standard 3-letter currency code to convert into (e.g., NPR, JPY, CAD)."
                }
            },
            "required": ["amount", "from_currency", "to_currency"]
        }
    }
}


CONTACTS_TOOL = {
    "type": "function",
    "function": {
        "name": "get_contact",
        "description": "Searches for a contact's email by their name. Supports partial name matching.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name or partial name of the contact to look up (e.g. 'john' or 'alice')."
                }
            },
            "required": ["name"]
        }
    }
}


EMAIL_TOOL = {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "Sends a simulated mock email to a specific recipient address.",
        "parameters": {
            "type": "object",
            "properties": {
                "recipient": {
                    "type": "string",
                    "description": "The verified target email address. CRITICAL: Never guess this parameter. "
                                   "You must extract this from the results of a prior 'get_contact' tool lookup."
                },
                "subject": {
                    "type": "string",
                    "description": "The clear title line text for the email subject."
                },
                "body": {
                    "type": "string",
                    "description": "The complete message body content text payload."
                }
            },
            "required": ["recipient", "subject", "body"]
        }
    }
}



TOOLS = [
    CALCULATOR_TOOL,
    CURRENT_TIME_TOOL,
    UNIT_CONVERTER_TOOL,
    WEATHER_TOOL,
    CURRENCY_CONVERTER_TOOL,
    CONTACTS_TOOL,
    EMAIL_TOOL
]