FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    MODEL_PATH=${MODEL_PATH:-/root/models/Llama-3.2-1B-Instruct} \
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

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create models directory
RUN mkdir -p models

# Expose the FastAPI port
EXPOSE 8081

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8081/health || exit 1

# Set the entrypoint
CMD ["python", "app/main.py"]
