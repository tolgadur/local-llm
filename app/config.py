from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_DIR = Path(os.path.expanduser(os.getenv("MODEL_DIR")))
TOKENIZER_PATH = str(MODEL_DIR / "tokenizer.model")
