""" Module that contains the main GitHub class """

import requests
from typing import Optional, List
from dataclasses import dataclass


class ConnectedObject:
    """ Base class for objects """

    def bind(self, github_object: "GitHub") -> None:
        self._github_connection = github_object


@dataclass
class Release:
    id: int
    name: str
    tag_name: str


@dataclass
class Tag:
    node_id: str
    name: str


@dataclass
class Repository(ConnectedObject):
    owner: str
    name: str
    id: int
    node_id: str

    def get_releases(self) -> List[Release]:
        """ Method to get the releases for this specific repo """

        releases = self._github_connection.api_call(
            f'repos/{self.owner}/{self.name}/releases'
        ).json()

        # Convert it to 'Release' objects
        resources = [
            Release(
                id=release['id'],
                name=release['name'],
                tag_name=release['tag_name']
            ) for release in releases
        ]

        # Return it
        return resources

    def get_tags(self) -> List[Release]:
        """ Method to get the releases for this specific repo """

        tags = self._github_connection.api_call(
            f'repos/{self.owner}/{self.name}/tags'
        ).json()

        # Convert it to 'Tag' objects
        resources = [
            Tag(
                node_id=tag['node_id'],
                name=tag['name']
            ) for tag in tags
        ]

        # Return it
        return resources


class GitHub:
    """ Class to interact with GitHub """

    def __init__(self, api_key: str) -> None:
        """ Sets default values """
        self.api_key = api_key
        self.session = requests.Session()

    def api_call(self, endpoint: str, method: str = 'GET', data: Optional[dict] = None) -> Optional[dict]:
        """ Run a API call to GitHub """

        # Prepare the request
        url = f'https://api.github.com/{endpoint}'
        request = requests.Request(method=method, url=url, json=data)
        prepared_request = self.session.prepare_request(request)

        # Run the request
        # TODO: Error reporting (try/except)
        return self.session.send(prepared_request)

    def get_repository(self, owner: str, repository: str) -> Repository:
        """ Retrieve a repository """
        response = self.api_call(f'repos/{owner}/{repository}')
        data = response.json()

        # Create a Repository object
        repo = Repository(
            owner=owner,
            name=repository,
            id=data['id'],
            node_id=data['node_id'])
        repo.bind(self)

        # Return the created repo
        return repo
