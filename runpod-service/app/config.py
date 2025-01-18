import os
from dotenv import load_dotenv

load_dotenv()

# Environment
TEST = os.getenv("TEST", "prod")
