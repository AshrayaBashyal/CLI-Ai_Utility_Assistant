from datetime import datetime


# **kwargs absorbs any random arguments the LLM invents, preventing a TypeError
def current_time(**kwargs) -> dict:
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