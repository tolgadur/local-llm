FROM python:3.11

# Build arguments for model configuration
ARG HUGGINGFACE_TOKEN
ARG MODEL_NAME=meta-llama/Llama-3.2-1B-Instruct-QLORA_INT4_EO8
ARG MODEL_DIR=/app/models/llama-3.2-1b

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    MODEL_PATH=${MODEL_DIR} \
    OMP_NUM_THREADS=${OMP_NUM_THREADS:-8} \
    MKL_NUM_THREADS=${MKL_NUM_THREADS:-8}

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies and huggingface_cli
RUN pip install --no-cache-dir -r requirements.txt

# Create model directory and download model if token is provided
RUN mkdir -p ${MODEL_DIR} && \
    if [ -n "$HUGGINGFACE_TOKEN" ]; then \
        huggingface-cli download --token ${HUGGINGFACE_TOKEN} \
            --local-dir ${MODEL_DIR} \
            ${MODEL_NAME} \
            --exclude "original/*"; \
    else \
        echo "Warning: HUGGINGFACE_TOKEN not provided. Model will not be downloaded during build."; \
    fi

# Copy the rest of the application
COPY . .

# Install the package in development mode
RUN pip install -e .

# Expose the FastAPI port
EXPOSE 8081

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8081/health || exit 1

# Set the entrypoint
CMD ["python", "app/main.py"]
