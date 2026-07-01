import requests 
from config import WEATHER_ACCESS_KEY

def get_weather(city: str) -> dict:
    if not city or not city.strip():
        return {"success": False, "error": {"message": "API Error: Please specify a valid location identifier using the query parameter."}}

    url = f"http://weatherstack.com{WEATHER_ACCESS_KEY}&query={city.strip()}"
    
    try:
        data = requests.get(url, timeout=10).json()
    except Exception:
        return {"success": False, "error": {"message": "Network or Parsing Error: Connection failed."}}

    if data.get("success") is False:
        return {"success": False, "error": {"message": f"API Error: {data.get('error', {}).get('info')}"}}

    current = data.get("current", {})
    
    return {
        "success": True, 
        "data": {
            "temperature": current.get("temperature"),
            "feels_like": current.get("feelslike"),
            "weather": current.get("weather_descriptions", ["Unknown"])[0].strip(),
            "humidity": current.get("humidity"),
            "wind_speed": current.get("wind_speed"),
            "precipitation": current.get("precip")
        }
    }
