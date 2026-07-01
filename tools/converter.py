LENGTH_UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
}


def convert(value: float, from_unit: str, to_unit: str) -> dict:
    try:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in LENGTH_UNITS:
            return {
                "success": False,
                "error": {
                    "message": f"Unsupported unit: {from_unit}"
                }
            }

        if to_unit not in LENGTH_UNITS:
            return {
                "success": False,
                "error": {
                    "message": f"Unsupported unit: {to_unit}"
                }
            }

        meters = value * LENGTH_UNITS[from_unit]
        result = meters / LENGTH_UNITS[to_unit]

        return {
            "success": True,
            "data": {
                "value": result,
                "unit": to_unit
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": {
                "message": str(e)
            }
        }