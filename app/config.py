from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
MAX_LENGTH = int(os.getenv("MAX_LENGTH", "2048"))
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
