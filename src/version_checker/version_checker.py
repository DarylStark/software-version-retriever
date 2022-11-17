from abc import abstractmethod, ABC
from typing import Optional


class VersionChecker(ABC):
    """ Base class for Current Version Checkers """

    def __init__(self) -> None:
        # Create a cache that the subclasses can use
        self.cache = dict()

    @abstractmethod
    def retrieve_version(self) -> Optional[str]:
        pass
