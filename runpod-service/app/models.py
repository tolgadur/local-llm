import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from app.config import MODEL_PATH
import logging
import os

logger = logging.getLogger(__name__)

MODEL_ID = "meta-llama/Llama-3.2-11B-Vision-Instruct"
MODEL_PATH = os.path.abspath(MODEL_PATH)

logger.info("=== Starting Model Initialization ===")
logger.info(f"Model path: {MODEL_PATH}")

# Load tokenizer and model once to share between pipelines
logger.info("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
logger.info("✓ Tokenizer loaded")

logger.info("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto",
)
logger.info("✓ Model loaded")

# Initialize both pipelines with shared model and tokenizer
logger.info("Initializing vision pipeline...")
LLAMA11B_VISION = pipeline(
    "image-text-to-text",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
)
logger.info("✓ Vision pipeline ready")

logger.info("Initializing text pipeline...")
LLAMA11B_TEXT = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="gpu",
)
logger.info("✓ Text pipeline ready")
logger.info("=== Model Initialization Complete ===\n")
