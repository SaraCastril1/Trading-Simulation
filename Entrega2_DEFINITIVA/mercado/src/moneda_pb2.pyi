from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class message_parameters(_message.Message):
    __slots__ = ["moneda", "periodo"]
    MONEDA_FIELD_NUMBER: _ClassVar[int]
    PERIODO_FIELD_NUMBER: _ClassVar[int]
    moneda: str
    periodo: str
    def __init__(self, moneda: _Optional[str] = ..., periodo: _Optional[str] = ...) -> None: ...

class ping(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ACK(_message.Message):
    __slots__ = ["ack"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: bool
    def __init__(self, ack: bool = ...) -> None: ...
