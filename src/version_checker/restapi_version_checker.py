import requests
from .version_checker import VersionChecker
from typing import Optional


class RestAPIVersionChecker(VersionChecker):
    """ Version Checker to use a REST API """

    def __init__(self,
                 method: str,
                 https: bool,
                 server: str,
                 port: str,
                 endpoint: str,
                 authentication: Optional[dict] = None,
                 extra_headers: Optional[dict] = None) -> None:
        """ Set configuration values """
        self.method = method
        self.https = https
        self.server = server
        self.port = port
        self.endpoint = endpoint
        self.authentication = authentication
        self.extra_headers = extra_headers

    def api_call(self) -> requests.Response:
        """ Method to do the API call """

        # Define the properties
        protocol = 'https' if self.https else 'http'
        url = f'{protocol}://{self.server}:{self.port}{self.endpoint}'
        headers = None
        if self.extra_headers:
            headers = self.extra_headers.copy()
        if self.authentication:
            if self.authentication['type'] == 'token':
                headers.update(
                    {'Authorization': f'Token {self.authentication["token"]}'})

        # Check if this is already cached
        cache_key = f'RestAPIVersionChecker_{self.method}_{url}'
        if cache_key in self.cache.keys():
            return self.cache[cache_key]

        # Run the request
        # TODO: Error reporting (try/except)
        request = requests.request(
            method=self.method,
            url=url,
            headers=headers)

        # Add it to the cache
        self.cache[cache_key] = request

        # Return the Request object
        return request
