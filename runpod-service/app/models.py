import torch
from transformers import pipeline
from app.config import MODEL_PATH
import logging
import os

logger = logging.getLogger(__name__)

MODEL_ID = "meta-llama/Llama-3.2-11B-Vision-Instruct"

logger.info(f"Loading model from path: {MODEL_PATH}")

LLAMA11B = pipeline(
    "image-text-to-text",
    model=os.path.abspath(MODEL_PATH),  # Use absolute path to local model
    torch_dtype=torch.float16,
    device_map="auto",  # Changed to auto for better device handling
)
