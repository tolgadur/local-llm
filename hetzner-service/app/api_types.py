from typing import Optional, Dict
from pydantic import BaseModel


class InternalGenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 100


class InternalRunpodRequest(BaseModel):
    """Request model for Runpod service calls"""

    text: str = None
    image: Optional[bytes] = None
    image_format: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class InternalRunpodResponse(BaseModel):
    """Response model for Runpod service calls"""

    success: bool
    error_message: Optional[str] = None
    text_result: str  # Not optional - will always be present on success
    image_data: Optional[bytes] = None
    image_format: Optional[str] = None
