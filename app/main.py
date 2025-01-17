from app.tokenizer import Tokenizer
from app.model import Model
from app.config import TOKENIZER_PATH


def main():
    tokenizer = Tokenizer(TOKENIZER_PATH)
    model = Model(tokenizer)

    # Example usage
    prompt = "Hello, how are you?"
    response = model.generate(prompt, max_length=100, temperature=0.8)
    print(response)


if __name__ == "__main__":
    main()
