import abc
from typing import Any


class BaseSendHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Application sends a line alert message without any arguments."""
        pass


class BaseSuccessHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Application sends a success message without any arguments."""
        pass


class BaseExceptionIpython(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def custom_exc(self, *args: Any, **kwargs: Any) -> Any:
        """Application sends exception message in ipython."""
        pass
