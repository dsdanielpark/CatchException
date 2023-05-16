import abc
from typing import Any

class BaseSendHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Application sends a success message without any arguments.
        """
        pass