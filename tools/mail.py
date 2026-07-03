from typing import Dict, Any

def send_email(recipient: str, subject: str, body: str) -> dict:
    try:
        to_address = str(recipient).strip()
        mail_subject = str(subject).strip()
        mail_body = str(body).strip()

        # Simple input verification guards
        if not to_address or "@" not in to_address:
            return {"success": False, "error": {"message": f"Invalid recipient address: '{recipient}'"}}
        if not mail_subject:
            return {"success": False, "error": {"message": "Email subject cannot be empty."}}

        # Log simulated action directly to your console
        print(f"\n[SIMULATION] Sending Email to: {to_address}")
        print(f"   [SUBJECT]: {mail_subject}")
        print(f"   [BODY]:\n{mail_body}\n" + "-"*40)

        return {
            "success": True,
            "data": {
                "status": "sent",
                "recipient": to_address
            }
        }
    except Exception as e:
        return {"success": False, "error": {"message": str(e)}}
