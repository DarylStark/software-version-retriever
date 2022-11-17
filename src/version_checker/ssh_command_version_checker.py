from .shell_command_version_checker import ShellCommandVersionChecker
import paramiko


class SSHCommandVersionChecker(ShellCommandVersionChecker):
    """ Version Checker for shell commands over SSH """

    def __init__(self,
                 remote_server: str,
                 username: str,
                 identity_file: Optional[str] = None,
                 timeout: int = 10,
                 **kwargs) -> None:
        """ Set configuration values """
        super().__init__(**kwargs)
        self.remote_server = remote_server
        self.username = username
        self.identity_file = identity_file
        self.timeout = timeout

    def get_command_output(self) -> str:
        """ Method to run the command on the remote host and retrieve the
            output """
        # Create a SSH clients
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(self.remote_server,
                    username=self.username,
                    key_filename=self.identity_file,
                    timeout=self.timeout)
        stdin, stdout, stderr = ssh.exec_command(self.command)
        lines = ''.join(stdout.readlines()).strip()
        return lines
