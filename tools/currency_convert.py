import requests
from typing import Dict, Any

def convert_currency(amount: float, from_currency: str,    to_currency: str) -> Dict[str, Any]:
    
    # Check basic inputs before doing anything else
    if not from_currency or not to_currency:
        return {
            "success": False,
            "error": { "message": "Both 'from_currency' and 'to_currency' must be provided." }
        }
        
    src = from_currency.strip().upper()
    dest = to_currency.strip().upper()
    
    if len(src) != 3 or len(dest) != 3:
        return {
            "success": False,
            "error": { "message": "Currency codes must be valid 3-letter ISO strings (e.g., USD)." }
        }
        
    if amount <= 0:
        return {
            "success": False,
            "error": { "message": f"Conversion amount must be greater than 0. Received: {amount}" }
        }
        
    # Skip the API request completely if currencies match
    if src == dest:
        return {
            "success": True,
            "data": {
                "from_currency": src,
                "to_currency": dest,
                "original_amount": float(amount),
                "converted_amount": float(amount),
                "exchange_rate": 1.0
            }
        }

    url = f"https://api.frankfurter.dev/v2/rate/{src}/{dest}"
    
    # Pre-define response so exception blocks don't throw NameErrors
    response = None
    
    # Fire the network request
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return { "success": False, "error": { "message": "The currency service timed out. Please try again." } }
    except requests.exceptions.ConnectionError:
        return { "success": False, "error": { "message": "Unable to connect to the currency service network." } }
    except requests.exceptions.HTTPError:
        # Check if the API returned a custom error message (like an invalid currency)
        if response is not None:
            try:
                err_json = response.json()
                if isinstance(err_json, dict) and "message" in err_json:
                    return { "success": False, "error": { "message": err_json["message"] } }
            except (ValueError, TypeError):
                pass
            return { "success": False, "error": { "message": f"HTTP Error {response.status_code}: {response.reason}" } }
        return { "success": False, "error": { "message": "An HTTP error occurred before data could be processed." } }
    except requests.exceptions.RequestException:
        return { "success": False, "error": { "message": "A network error occurred while fetching currency data." } }

    # Extract JSON body
    try:
        data = response.json()
    except (ValueError, TypeError):
        return { "success": False, "error": { "message": "Received invalid response data format." } }

    # Double check that the required data fields exist
    if not isinstance(data, dict) or not all(k in data for k in ["base", "quote", "rate"]):
        return { "success": False, "error": { "message": "Currency conversion data is currently unavailable." } }

    # Calculate final value and return
    try:
        exchange_rate = float(data["rate"])
        return {
            "success": True,
            "data": {
                "from_currency": data.get("base"),
                "to_currency": data.get("quote"),
                "original_amount": float(amount),
                "converted_amount": round(amount * exchange_rate, 4),
                "exchange_rate": exchange_rate
            }
        }
    except (ValueError, TypeError):
        return { "success": False, "error": { "message": "Could not parse numerical rate values from response data." } }