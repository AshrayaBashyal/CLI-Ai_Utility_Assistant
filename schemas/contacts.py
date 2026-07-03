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