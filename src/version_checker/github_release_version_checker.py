import requests
import re
from .version_checker import VersionChecker
from typing import Optional
from github_api import GitHub


class GitHubReleaseVersionChecker(VersionChecker):
    """ Version Checker to use a REST API """

    def __init__(self,
                 owner: str,
                 repository: bool,
                 token: str,
                 name_regex: Optional[str] = None) -> None:
        """ Set configuration values """
        self.owner = owner
        self.repository = repository
        self.token = token
        self.name_regex = name_regex

    def retrieve_version(self) -> str:
        """ Retrieve the version """

        # Create a GitHub object and retrieve the repository and the releases
        gh = GitHub(api_key=self.token)
        repo = gh.get_repository(self.owner, self.repository)
        releases = repo.get_releases()

        # Get the latests release-name
        latest_release_name = releases[0].name

        # Run the regex
        if self.name_regex:
            matches = re.findall(self.name_regex, latest_release_name)
            if len(matches) == 1:
                latest_release_name = matches[0]

        # Return the version
        return latest_release_name
