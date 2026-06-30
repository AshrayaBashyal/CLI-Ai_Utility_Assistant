from datetime import datetime


def current_time() -> dict:
    try:
        return {
            "success": True,
            "data": {
                "time": datetime.now().strftime("%I:%M:%S %p")
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": {
                "message": str(e)
            }
        }