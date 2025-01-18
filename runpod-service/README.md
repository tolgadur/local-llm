# RunPod LLM Service

A serverless service designed to run large language models on RunPod's infrastructure, providing scalable inference capabilities.

## Project Structure

```plaintext
runpod-service/
├── app/
│   ├── __init__.py
│   └── main.py      # RunPod serverless handler and model logic
├── .env             # Environment variables (not in git)
├── Dockerfile
└── requirements.txt
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

Create a `.env` file with:

```bash
RUNPOD_API_KEY=your_api_key
MODEL_PATH=/path/to/model
HUGGINGFACE_TOKEN=your_token_here  # If using Hugging Face models
```

## Development

1. Local Testing:

```bash
# Set up test environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Run the handler locally
python app/main.py
```

Test the handler function:

```python
from app.main import handler

# Test with sample input
result = handler({"input": {"prompt": "Hello, how are you?"}})
print(result)
```

## Deployment

Build the Docker image:

```bash
docker build -t your-registry/runpod-service:latest .
```

Push to your container registry:

```bash
docker push your-registry/runpod-service:latest
```

Deploy on RunPod:

- Go to RunPod Serverless dashboard
- Create a new endpoint using your container image
- Configure the endpoint with appropriate GPU and memory settings
- Set your environment variables in the RunPod dashboard

## API Usage

Once deployed, you can use the RunPod API to make inference requests:

```python
import runpod

runpod.api_key = "your_api_key"
endpoint = runpod.Endpoint("your_endpoint_id")

# Synchronous request
result = endpoint.run({"prompt": "Hello, how are you?"})
print(result)

# Async request
job = endpoint.run_async({"prompt": "Hello, how are you?"})
result = job.wait_for_output()
print(result)
```
