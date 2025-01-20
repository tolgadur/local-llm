import os
from dotenv import load_dotenv

load_dotenv()

GRPC_PORT = int(os.getenv("GRPC_PORT", "50051"))
MODEL_PATH = os.getenv("MODEL_PATH", "/tmp/models/llama-vision")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
