import requests
from config import WEATHER_ACCESS_KEY

def get_weather(city: str) -> dict:
    # Input Validation
    if not city or not isinstance(city, str) or not city.strip():
        return {
            "success": False,
            "error": {"message": "City name cannot be empty."}
        }

    # URL Construction
    url = (
        "http://api.weatherstack.com/current"
        f"?access_key={WEATHER_ACCESS_KEY}"
        f"&query={city.strip()}"
    )
    
    # Network Request Layer 
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Catches 404, 500, etc.forces Python to raise a requests.exceptionHTTPError.
    except requests.exceptions.Timeout:
        return {"success": False, "error": {"message": "The weather service timed out. Please try again."}}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": {"message": "Unable to connect to the weather service network."}}
    except requests.exceptions.RequestException:   # HTTPError is a subclass of RequestException 
        return {"success": False, "error": {"message": "A network error occurred while fetching weather data."}}

    # JSON Parsing 
    try:
        data = response.json()
    except ValueError:
        return {"success": False, "error": {"message": "Received invalid response data format."}}

    # 5. External API Application Error Handling
    if data.get("success") is False:
        error_info = data.get("error", {})
        error_code = error_info.get("code")
        
        if error_code == 615:
            msg = "City not found. Please verify the location spelling."
        else:
            msg = "Unable to retrieve weather information at this time."
            
        return {"success": False, "error": {"message": msg}}

    # 6. Defensive Structural Verification
    if "location" not in data or "current" not in data:
        return {"success": False, "error": {"message": "Weather data format is currently unavailable."}}

    location = data.get("location", {})
    current = data.get("current", {})

    # Extract weather description list safely
    descriptions = current.get("weather_descriptions", [])
    condition = ", ".join(str(item).strip() for item in descriptions if str(item).strip()) if isinstance(descriptions, list) and descriptions else "Unknown"
    # condition = descriptions[0].strip() if isinstance(descriptions, list) and descriptions else "Unknown"

    # 7. Final Payload Formatting
    return {
        "success": True,
        "data": {
            "city": location.get("name"),
            "country": location.get("country"),
            "temperature": current.get("temperature"),
            "feels_like": current.get("feelslike"),
            "condition": condition,
            "humidity": current.get("humidity"),
            "wind_speed": current.get("wind_speed"),
            "precipitation": current.get("precip")
        }
    }
