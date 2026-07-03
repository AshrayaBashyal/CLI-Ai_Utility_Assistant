from tools.calculator import calculator
from tools.time import current_time
from tools.converter import convert
from tools.weather import get_weather
from tools.currency_convert import convert_currency
from tools.contacts import get_contact
from tools.mail import send_email


TOOL_REGISTRY = {
    "calculator": calculator,
    "current_time" : current_time,
    "convert" : convert,
    "get_weather" : get_weather,
    "convert_currency" : convert_currency,
    "get_contact" : get_contact,
    "send_email" : send_email
}