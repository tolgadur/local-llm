from setuptools import setup, find_packages

setup(
    name="local-llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "accelerate",
        "sentencepiece",
        "pytest",
        "python-dotenv",
        "datasets",
        "evaluate",
        "tqdm",
    ],
)
