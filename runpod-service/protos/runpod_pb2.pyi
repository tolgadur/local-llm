from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RunpodRequest(_message.Message):
    __slots__ = ("text", "image_data", "image_format", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    text: str
    image_data: bytes
    image_format: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, text: _Optional[str] = ..., image_data: _Optional[bytes] = ..., image_format: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RunpodResponse(_message.Message):
    __slots__ = ("text_result", "image_data", "image_format", "success", "error_message")
    TEXT_RESULT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    text_result: str
    image_data: bytes
    image_format: str
    success: bool
    error_message: str
    def __init__(self, text_result: _Optional[str] = ..., image_data: _Optional[bytes] = ..., image_format: _Optional[str] = ..., success: bool = ..., error_message: _Optional[str] = ...) -> None: ...
