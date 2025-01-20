import torch
import os
from transformers import pipeline
from app.config import MODEL_PATH, HUGGINGFACE_TOKEN
import logging

logger = logging.getLogger(__name__)

MODEL_ID = "meta-llama/Llama-3.2-11B-Vision-Instruct"

# Create model directory if it doesn't exist
os.makedirs(MODEL_PATH, exist_ok=True)

logger.info(f"Initializing model {MODEL_ID}")
logger.info(f"Model will be saved to {MODEL_PATH}")

LLAMA11B = pipeline(
    "image-text-to-text",
    model=MODEL_ID,  # Use model ID instead of local path
    torch_dtype=torch.float16,
    device_map="cuda",
    token=HUGGINGFACE_TOKEN,
    cache_dir=MODEL_PATH,  # This will download and cache the model
)
