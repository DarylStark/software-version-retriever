import requests
import re
from .github_version_checker import GitHubVersionChecker
from typing import Optional
from github_api import GitHub


class GitHubTagVersionChecker(GitHubVersionChecker):
    """ Version Checker to use GitHub tags """

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
        cache_key = f'GitHubTagVersionChecker_{self.owner}_{self.repository}'
        if cache_key in self.cache.keys():
            tags = self.cache[cache_key]
        else:
            # Get the tags
            tags = self.repository_object.get_tags()
            self.cache[cache_key] = tags

        # Get the latests release-name
        latest_tag_name = tags[0].name

        # Run the regex
        if self.name_regex:
            for tag in tags:
                matches = re.findall(self.name_regex, tag.name)
                if len(matches) == 1:
                    latest_tag_name = matches[0]
                    break

        # Replace underscores with dots
        if self.replace_underscores:
            latest_tag_name = latest_tag_name.replace('_', '.')

        # Return the version
        return latest_tag_name
