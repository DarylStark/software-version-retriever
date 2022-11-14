import requests
import re
from .github_version_checker import GitHubVersionChecker
from typing import Optional
from github_api import GitHub


class GitHubTagVersionChecker(GitHubVersionChecker):
    """ Version Checker to use GitHub tags """

    def __init__(self,
                 name_regex: Optional[str] = None,
                 **kwargs) -> None:
        """ Set configuration values """
        super().__init__(**kwargs)
        self.name_regex = name_regex

    def retrieve_version(self) -> str:
        """ Retrieve the version """

        # Get the releases
        tags = self.repository_object.get_tags()

        # Get the latests release-name
        latest_tag_name = tags[0].name

        # Run the regex
        if self.name_regex:
            matches = re.findall(self.name_regex, latest_tag_name)
            if len(matches) == 1:
                latest_tag_name = matches[0]

        # Return the version
        return latest_tag_name
