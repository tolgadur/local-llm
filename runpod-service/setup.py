from setuptools import setup, find_packages

setup(
    name="runpod-llm-service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "runpod==1.5.0",
        "transformers>=4.36.0",
        "torch>=2.1.0",
        "numpy>=1.24.0",
        "python-dotenv>=1.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="RunPod serverless service for LLM inference",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
