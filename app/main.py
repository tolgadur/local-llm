from app.local_model import LocalModel


def main():
    model = LocalModel()

    # Test with a simple prompt
    prompt = "What is machine learning?"

    try:
        response = model.generate(prompt=prompt)
        print("\nResponse:", response)
    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()
