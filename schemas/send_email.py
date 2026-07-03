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