import torch
from transformers import pipeline
from config import MODEL_PATH, HUGGINGFACE_TOKEN

LOCAL_MODEL_CPU = pipeline(
    "text-generation",
    model=MODEL_PATH,
    torch_dtype=torch.float32,
    device_map="cpu",
    token=HUGGINGFACE_TOKEN,
    model_kwargs={"low_cpu_mem_usage": True},
)
