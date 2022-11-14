import subprocess
from .github_version_checker import GitHubVersionChecker
from typing import Optional


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
        output = self.get_command_output()

        # TODO: Parse name_regex
        return output
