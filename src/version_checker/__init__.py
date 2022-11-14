# Base class for Version Checkers
from .version_checker import VersionChecker

# Classes to retrieve from REST APIs
from .restapi_version_checker import RestAPIVersionChecker
from .restapi_json_version_checker import RestAPIJSONVersionChecker

# Classes to retrieve from GitHub
from .github_version_checker import GitHubVersionChecker
from .github_release_version_checker import GitHubReleaseVersionChecker
from .github_tag_version_checker import GitHubTagVersionChecker
