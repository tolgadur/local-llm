from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.config import MODEL_NAME, MAX_LENGTH, HUGGINGFACE_TOKEN


class LocalModel:
    def __init__(self):
        """Initialize the model and tokenizer using transformers."""
        print(f"Loading model {MODEL_NAME}...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME, use_auth_token=HUGGINGFACE_TOKEN
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float32,
            device_map="auto",
            low_cpu_mem_usage=True,
            use_auth_token=HUGGINGFACE_TOKEN,
        )
        print("Model loaded successfully")

    def generate(
        self, prompt: str, max_length: int = MAX_LENGTH, temperature: float = 0.7
    ) -> str:
        """Generate text based on the input prompt.

        Args:
            prompt: The input text to generate from
            max_length: Maximum number of tokens to generate
            temperature: Controls randomness in generation. Lower is more focused.
                Range is 0.0 to 2.0.

        Returns:
            Generated text as string
        """
        inputs = self.tokenizer(
            prompt, return_tensors="pt", return_token_type_ids=False
        )
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}

        # Generate with simpler parameters
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                temperature=temperature,
                do_sample=True,
            )

        # Decode and return
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
