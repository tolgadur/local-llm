# Local LLM API

A FastAPI service that runs LLama models locally for text generation.

## Project Structure

local-llm/
├── app/
│   ├── config.py      # Environment and configuration settings
│   ├── main.py        # FastAPI application and endpoints
│   └── models.py      # Model initialization and pipeline setup
├── .env               # Environment variables (not in git)
├── Dockerfile
└── README.md

## Setup

1. Create a `.env` file with your configuration:

```bash
MODEL_PATH=/root/models/Llama-3.2-1B-Instruct
HUGGINGFACE_TOKEN=your_token_here
```

## Running the Application

To build and run the Docker container, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t local-llm .
   ```

2. Run the Docker container with a volume reference to your model:

   ```bash
   docker run -d --env-file .env -v /root/models:/root/models -p 8081:8081 local-llm
   ```

Replace `/root/models` with the actual path to your model directory on your host machine.

## Accessing the API

Once the container is running, you can access the FastAPI application at `http://localhost:8081`.

You can use the `curl` command to test the API:

```bash
curl -X POST http://95.217.106.119:8081/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a short poem about coding:", "max_length": 100}' | jq
```
