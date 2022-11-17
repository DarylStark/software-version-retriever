from abc import abstractmethod, ABC
from typing import Optional


class VersionChecker(ABC):
    """ Base class for Current Version Checkers """

    cache = dict()

    @abstractmethod
    def retrieve_version(self) -> Optional[str]:
        pass
