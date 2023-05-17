import abc
from typing import Any


class BaseExceptionIpython(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def custom_exc(self, *args: Any, **kwds: Any) -> Any:
        """Application sends a exception message."""
        pass
