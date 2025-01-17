import pytest
from app.tokenizer import Tokenizer
from app.config import TOKENIZER_PATH


@pytest.fixture
def tokenizer():
    return Tokenizer(TOKENIZER_PATH)


def test_encode_decode_roundtrip(tokenizer):
    """Test that encoding and then decoding preserves the original text."""
    original_text = "Hello, this is a test string with some special chars: @#$%^&*"
    tokens = tokenizer.encode(original_text)
    decoded_text = tokenizer.decode(tokens)
    assert decoded_text == original_text


def test_encode_decode_multiple_roundtrip(tokenizer):
    """Test encoding and decoding preserves multiple original texts."""
    original_texts = [
        "Hello world",
        "This is another test",
        "Special characters: @#$%^&*",
        "A longer piece of text that should be preserved correctly.",
    ]
    tokens = tokenizer.encode(original_texts)
    decoded_texts = tokenizer.decode(tokens)
    assert decoded_texts == original_texts


def test_invalid_model_path():
    """Test initialization with invalid model path."""
    with pytest.raises(Exception):
        Tokenizer("invalid/path/to/model.model")
