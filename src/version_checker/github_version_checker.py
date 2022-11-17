import requests
import re
from .version_checker import VersionChecker
from typing import Optional
from github_api import GitHub


class GitHubVersionChecker(VersionChecker):
    """ Version Checker for GitHub """

    def __init__(self,
                 owner: str,
                 repository: bool,
                 token: str) -> None:
        """ Set configuration values """
        super().__init__()

        self.owner = owner
        self.repository = repository
        self.token = token
        self.github_object = GitHub(api_key=self.token)
        self.repository_object = self.github_object.get_repository(
            self.owner, self.repository)
