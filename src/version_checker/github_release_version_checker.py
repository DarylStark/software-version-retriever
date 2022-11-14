import requests
import re
from .github_version_checker import GitHubVersionChecker
from typing import Optional
from github_api import GitHub


class GitHubReleaseVersionChecker(GitHubVersionChecker):
    """ Version Checker to use a REST API """

    def __init__(self,
                 name_regex: Optional[str] = None,
                 **kwargs) -> None:
        """ Set configuration values """
        super().__init__(**kwargs)
        self.name_regex = name_regex

    def retrieve_version(self) -> str:
        """ Retrieve the version """

        # Get the releases
        releases = self.repository_object.get_releases()

        # Get the latests release-name
        latest_release_name = releases[0].name

        # Run the regex
        if self.name_regex:
            matches = re.findall(self.name_regex, latest_release_name)
            if len(matches) == 1:
                latest_release_name = matches[0]

        # Return the version
        return latest_release_name
