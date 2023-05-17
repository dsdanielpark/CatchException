import abc
from typing import Any


class BaseSuccessHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Application sends a line alert message without any arguments."""
        pass
