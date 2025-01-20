import torch
from transformers import pipeline
from app.config import MODEL_PATH
import logging

logger = logging.getLogger(__name__)

MODEL_ID = "meta-llama/Llama-3.2-11B-Vision-Instruct"

logger.info(f"Loading model from {MODEL_PATH}")

LLAMA11B = pipeline(
    "image-text-to-text",
    model=MODEL_PATH,  # Use local path instead of model ID
    torch_dtype=torch.float16,
    device_map="cuda",
)
