# Base class for Version Checkers
from .version_checker import VersionChecker

# Classes to retrieve from REST APIs
from .restapi_version_checker import RestAPIVersionChecker
from .restapi_json_version_checker import RestAPIJSONVersionChecker
from .restapi_html_version_checker import RestAPIHTMLVersionChecker

# Classes to retrieve from GitHub
from .github_version_checker import GitHubVersionChecker
from .github_release_version_checker import GitHubReleaseVersionChecker
from .github_tag_version_checker import GitHubTagVersionChecker

# Classes to retrieve from shell commands
from .shell_command_version_checker import ShellCommandVersionChecker
from .ssh_command_version_checker import SSHCommandVersionChecker
