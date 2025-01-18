# Local LLM Services

This monorepo contains services for deploying and managing local large language models across different cloud platforms.

## Project Structure

```plaintext
.
├── hetzner-service/     # Main LLM service running on Hetzner Cloud
│   ├── app/
│   ├── models/
│   ├── tests/
│   └── ...
└── runpod-service/      # Serverless LLM service on RunPod
    ├── app/
    └── ...
```

## Services

### Hetzner Service

Located in `/hetzner-service`

- Main service for running and managing LLMs on Hetzner Cloud
- FastAPI-based REST API for model inference
- Supports multiple model formats and configurations
- Optimized for dedicated GPU instances
- See [hetzner-service/README.md](hetzner-service/README.md) for setup and deployment

### RunPod Service

Located in `/runpod-service`

- Serverless service for running LLMs on RunPod's infrastructure
- Event-driven architecture for scalable inference
- Pay-per-use pricing model
- Automatic scaling based on demand
- See [runpod-service/README.md](runpod-service/README.md) for setup and deployment

## Development

Each service has its own development environment and requirements. Please refer to the individual service READMEs for specific setup instructions.

### Common Setup Steps

Clone the repository:

```bash
git clone https://github.com/yourusername/local-llm.git
cd local-llm
```

Choose a service to work on and follow its README instructions

### Development Guidelines

- Each service maintains its own virtual environment
- Follow Python best practices (PEP 8)
- Write tests for new features
- Keep dependencies up to date
- Document API changes

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Write/update tests
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.
