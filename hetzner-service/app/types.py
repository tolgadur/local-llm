from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class RunpodRequest:
    text: Optional[str] = None
    image_data: Optional[bytes] = None
    image_format: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


@dataclass
class RunpodResponse:
    success: bool
    error_message: str
    text_result: Optional[str] = None
    image_data: Optional[bytes] = None
    image_format: Optional[str] = None
