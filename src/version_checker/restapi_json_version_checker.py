from version_checker.restapi_version_checker import RestAPIVersionChecker
from typing import Optional


class RestAPIJSONVersionChecker(RestAPIVersionChecker):
    """ Current Version Checker to use a REST API with JSON response """

    def __init__(self,
                 key: str,
                 **kwargs) -> None:
        """ Set configuration values """
        super().__init__(**kwargs)
        self.key = key

    def retrieve_version(self) -> Optional[str]:
        """ Method to get the version """
        response = self.api_call()
        json_data = response.json()
        if (self.key in json_data.keys()):
            return json_data[self.key]
        return None
