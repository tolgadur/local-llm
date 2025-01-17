import torch
from transformers import pipeline
from config import MODEL_PATH, HUGGINGFACE_TOKEN


def main():
    local_model_cpu = pipeline(
        "text-generation",
        model=MODEL_PATH,
        torch_dtype=torch.float32,
        device_map="cpu",
        token=HUGGINGFACE_TOKEN,
        model_kwargs={"low_cpu_mem_usage": True},
    )

    prompt = "What is machine learning?"
    response = local_model_cpu(prompt, max_new_tokens=50)
    print(response)


if __name__ == "__main__":
    main()
