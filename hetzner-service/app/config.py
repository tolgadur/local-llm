from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
MODEL_PATH = os.getenv("MODEL_PATH")

# Verify model path exists
if not os.path.exists(MODEL_PATH):
    raise ValueError(f"Model path does not exist: {MODEL_PATH}")
