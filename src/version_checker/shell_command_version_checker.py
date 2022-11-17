import subprocess
from .github_version_checker import GitHubVersionChecker
from typing import Optional
import re


class ShellCommandVersionChecker(GitHubVersionChecker):
    """ Version Checker for shell commands """

    def __init__(self,
                 command: str,
                 name_regex: Optional[str] = None) -> None:
        """ Set configuration values """
        self.command = command
        self.name_regex = name_regex

    def get_command_output(self) -> str:
        """ Method to run the command and retrieve the output """
        command = subprocess.run(self.command.split(), stdout=subprocess.PIPE)
        return command.stdout.decode('utf-8').strip()

    def retrieve_version(self) -> str:
        """ Retrieve the version """
        latest_release_name = self.get_command_output()

        # Run the regex
        if self.name_regex:
            matches = re.findall(self.name_regex, latest_release_name)
            if len(matches) == 1:
                latest_release_name = matches[0]

        # Return the version
        return latest_release_name
