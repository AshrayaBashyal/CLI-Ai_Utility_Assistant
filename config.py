from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")
WEATHER_ACCESS_KEY = os.getenv("WEATHER_ACCESS_KEY")