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
