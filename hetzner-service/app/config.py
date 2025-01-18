import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
MODEL_PATH = os.getenv("MODEL_PATH")
RUNPOD_HOST = os.getenv("RUNPOD_HOST", "localhost")
RUNPOD_PORT = int(os.getenv("RUNPOD_PORT", "50051"))
