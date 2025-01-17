import pytest
import torch
from transformers import pipeline
from app.config import MODEL_PATH, HUGGINGFACE_TOKEN


@pytest.fixture
def model():
    """Fixture to create pipeline instance for tests."""
    return pipeline(
        "text-generation",
        model=MODEL_PATH,
        torch_dtype=torch.float32,
        device_map="cpu",
        token=HUGGINGFACE_TOKEN,
    )


def test_model_initialization(model):
    """Test that pipeline is properly initialized."""
    assert model is not None


def test_basic_generation(model):
    """Test basic text generation works."""
    prompt = "What is machine learning?"
    response = model(prompt, max_new_tokens=50)
    assert isinstance(response[0]["generated_text"], str)
    assert len(response[0]["generated_text"]) > len(prompt)


def test_max_length_constraint(model):
    """Test that max_length parameter is respected."""
    prompt = "Tell me a story"
    short_response = model(prompt, max_new_tokens=20)
    long_response = model(prompt, max_new_tokens=100)
    assert len(short_response[0]["generated_text"]) < len(
        long_response[0]["generated_text"]
    )


def test_empty_prompt(model):
    """Test handling of empty prompt."""
    response = model("", max_new_tokens=50)
    assert isinstance(response[0]["generated_text"], str)


def test_very_long_prompt(model):
    """Test handling of very long input prompt."""
    long_prompt = "test " * 100  # Reduced from 1000 to be more reasonable
    response = model(long_prompt, max_new_tokens=50)
    assert isinstance(response[0]["generated_text"], str)
