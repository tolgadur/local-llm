import os
from dotenv import load_dotenv

load_dotenv()


GRPC_PORT = int(os.getenv("GRPC_PORT", "50051"))
