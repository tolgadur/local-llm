from setuptools import setup, find_packages

setup(
    name="hetzner-llm-service",
    version="0.1.0",
    description="A FastAPI service for local LLM inference",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "accelerate",
        "python-dotenv",
        "sentencepiece",
        "pytest",
        "evaluate",
        "fastapi",
        "uvicorn[standard]",
        "pydantic",
        "grpcio",
        "grpcio-tools",
        "protobuf",
    ],
    dependency_links=["https://download.pytorch.org/whl/cpu"],
)
