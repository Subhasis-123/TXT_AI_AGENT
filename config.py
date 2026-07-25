from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).parent

OUTPUT_FOLDER = BASE_DIR / "output"
TEMP_FOLDER = BASE_DIR / "temp"

MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:latest")