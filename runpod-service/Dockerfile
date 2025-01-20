FROM runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel

# Build arguments for model configuration
ARG MODEL_DIR=/tmp/models/llama-vision

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
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies and huggingface_cli
RUN pip install --no-cache-dir -r requirements.txt

# Create model directory
RUN mkdir -p ${MODEL_DIR} && chmod 777 ${MODEL_DIR}

# Copy the rest of the application
COPY . .

# Install the package in development mode
RUN pip install -e .

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8081/health || exit 1

# Set the entrypoint
CMD ["python", "app/main.py"] 
