import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "YouTube AI Learning Assistant"
APP_VERSION = "2.0"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env"
    )