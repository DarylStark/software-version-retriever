import requests
import re
from .github_version_checker import GitHubVersionChecker
from typing import Optional
from github_api import GitHub


class GitHubReleaseVersionChecker(GitHubVersionChecker):
    """ Version Checker to use GitHub releases """

    def __init__(self,
                 name_regex: Optional[str] = None,
                 replace_underscores: Optional[bool] = False,
                 **kwargs) -> None:
        """ Set configuration values """
        super().__init__(**kwargs)
        self.name_regex = name_regex
        self.replace_underscores = replace_underscores

    def retrieve_version(self) -> str:
        """ Retrieve the version """

        # Check if this is already cached
        cache_key = f'GitHubReleaseVersionChecker{self.owner}_{self.repository}'
        if cache_key in self.cache.keys():
            releases = self.cache[cache_key]
        else:
            # Get the releases
            releases = self.repository_object.get_releases()
            self.cache[cache_key] = releases

        # Get the latests release-name
        latest_release_name = releases[0].name

        # Run the regex
        if self.name_regex:
            for release in releases:
                matches = re.findall(self.name_regex, release.name)
                if len(matches) == 1:
                    latest_release_name = matches[0]
                    break

        # Replace underscores with dots
        if self.replace_underscores:
            latest_release_name = latest_tag_name.replace('_', '.')

        # Return the version
        return latest_release_name
