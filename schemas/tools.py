
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


CONVERTER_TOOL = {
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



TOOLS = [
    CALCULATOR_TOOL,
    CURRENT_TIME_TOOL,
]