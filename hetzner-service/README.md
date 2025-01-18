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
├── tests/            # Test suite
├── .env              # Environment variables (not in git)
├── Dockerfile
├── requirements.txt
└── setup.py
```

## Setup

Create a `.env` file with your configuration:

```bash
MODEL_PATH=/path/to/model
HUGGINGFACE_TOKEN=your_token_here
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Development

1. Run tests:

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

Access the FastAPI application at `http://your-server:8081`.

Example request:

```bash
curl -X POST http://your-server:8081/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a short poem about coding:", "max_length": 100}'
```
