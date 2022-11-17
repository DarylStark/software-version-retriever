from version_checker.restapi_version_checker import RestAPIVersionChecker
from typing import Optional
import re


class RestAPIHTMLVersionChecker(RestAPIVersionChecker):
    """ Current Version Checker to use a REST API with JSON response """

    def __init__(self,
                 name_regex: Optional[str] = None,
                 **kwargs) -> None:
        """ Set configuration values """
        super().__init__(**kwargs)
        self.name_regex = name_regex

    def retrieve_version(self) -> Optional[str]:
        """ Method to get the version """
        response = self.api_call()
        body = response.text

        # Run the regex
        if self.name_regex:
            matches = re.findall(self.name_regex, body)
            if len(matches) == 1:
                body = matches[0]

        # Return the response
        return body
