# Hetzner LLM Service

A FastAPI service that runs LLama models on Hetzner Cloud infrastructure for efficient text generation.

## Project Structure

```plaintext
hetzner-service/
├── app/
│   ├── __init__.py
│   ├── config.py      # Environment and configuration settings
│   ├── main.py        # FastAPI application and endpoints
│   └── models.py      # Model initialization and pipeline setup
├── models/            # Directory for model files
├── protos/           # Generated gRPC code
├── tests/            # Test suite
├── .env              # Environment variables (not in git)
├── Dockerfile
├── requirements.txt
└── setup.py
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate gRPC code from proto file:

```bash
python -m grpc_tools.protoc -I../shared/protos --python_out=./protos --grpc_python_out=./protos ../shared/protos/runpod.proto
```

Configure environment variables:

```bash
MODEL_PATH=/path/to/model
HUGGINGFACE_TOKEN=your_token_here
RUNPOD_HOST=localhost
RUNPOD_PORT=50051
```

Start the service:

```bash
PYTHONPATH=. python -m app.main
```

## Development

Run tests:

```bash
pytest tests/
```

Start the development server:

```bash
uvicorn app.main:app --reload --port 8081
```

## Deployment

Build the Docker image:

```bash
docker build -t hetzner-llm-service .
```

Run on Hetzner:

```bash
docker run -d --env-file .env \
  -v /path/to/models:/app/models \
  -p 8081:8081 hetzner-llm-service
```

## API Usage

### REST API

Access the FastAPI application at `http://your-server:8081`.

Example request:

```bash
curl -X POST http://your-server:8081/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a short poem about coding:", "max_length": 100}'
```

```bash
curl -X POST http://your-servrr:8081/runpod/process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your text input here",
    "image": null,
    "image_format": null,
    "parameters": {
      "key1": "value1",
      "key2": "value2"
    }
  }'
```

### gRPC Interface

The service connects to the RunPod service via gRPC for text and image processing. See the proto definition in `shared/protos/runpod.proto` for the API specification.
