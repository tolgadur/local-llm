FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MODEL_PATH=/app/models/Llama-3.2-1B-Instruct \
    PYTHONPATH=/app \
    OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
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

# Set the entrypoint
CMD ["python", "app/main.py"]
