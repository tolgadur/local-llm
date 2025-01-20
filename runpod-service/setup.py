from setuptools import setup, find_packages

setup(
    name="runpod-llm-service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "runpod",
        "transformers",
        "torch",
        "numpy",
        "python-dotenv",
        "grpcio",
        "grpcio-tools",
        "protobuf",
        "grpcio-reflection",
        "accelerate",
        "bitsandbytes",
        "sentencepiece",
        "pillow",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="RunPod serverless service for LLM inference",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
