from setuptools import setup, find_packages

setup(
    name="local-llm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "accelerate",
        "python-dotenv",
        "sentencepiece",
        "pytest",
        "evaluate",
    ],
    dependency_links=["https://download.pytorch.org/whl/cpu"],
)
