from tools.calculator import calculator
from tools.time import current_time
from tools.converter import convert
from tools.weather import get_weather
from tools.currency_convert import convert_currency


TOOL_REGISTRY = {
    "calculator": calculator,
    "current_time" : current_time,
    "convert" : convert,
    "get_weather" : get_weather,
    "convert_currency" : convert_currency
}