import torch
import os
from transformers import pipeline
from app.config import MODEL_PATH, HUGGINGFACE_TOKEN

if not os.path.exists(MODEL_PATH):
    raise ValueError(
        f"Model path {MODEL_PATH} does not exist. "
        "Please make sure the model is downloaded."
    )

LOCAL_MODEL_CPU = pipeline(
    "text-generation",
    model=MODEL_PATH,
    torch_dtype=torch.float32,
    device_map="cpu",
    token=HUGGINGFACE_TOKEN,
    model_kwargs={"low_cpu_mem_usage": True},
    return_full_text=False,
)
