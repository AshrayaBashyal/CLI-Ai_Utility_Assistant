from tools.calculator import calculator
from tools.time import current_time
from tools.converter import convert


TOOL_REGISTRY = {
    "calculator": calculator,
    "current_time" : current_time,
    "convert" : convert
}