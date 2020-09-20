import paramiko
import re

class cmd_object():
    def __init__(self, hostname):
        self.hostname = hostname
        self.commands = {}

    def cmd_validator(self, output, regex):
        for line in output:
            ret = re.search(regex, line)
            if ret is not None:
                return "failed"
        return "success"

    def formatOutput(self, output):
        formatted_string = ""
        for line in output:
            stripped_line = line.split()
            fmt_line = ' '.join(stripped_line)
            formatted_string += fmt_line + "\n"
        return formatted_string

    def cmd_status(self, cmd, result, output, regex):
        validation_result = self.cmd_validator(output, regex)
        fmt_output = self.formatOutput(output)
        self.commands[cmd] = {
                                "submit_config_result": result,
                                "device_output": fmt_output,
                                "device_accepted_result": validation_result
                             }


class DeviceConfig():
    def __init__(self, hostname, username, password, cmd_validation_regex):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.cmd_validation_regex = cmd_validation_regex
        self.cmd_results = {}

    def runCommands(self, cmd_list):
        ssh_ctx = paramiko.SSHClient()
        ssh_ctx.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_ctx.connect(hostname=self.hostname, username=self.username, password=self.password, look_for_keys=False)
        device = cmd_object(self.hostname)

        for cmd in cmd_list:
            stdin, stdout, stderr = ssh_ctx.exec_command(cmd)
            stdin = stdin.channel.makefile_stdin()
            stderr = stderr.channel.makefile_stderr()

            stdin_list = [line for line in stdin.readlines()]
            stderr_list = [line for line in stderr.readlines()]

            if len(stdin_list) > 0:
                device.cmd_status(cmd, "success", stdin_list, self.cmd_validation_regex)

            if len(stderr_list) > 0:
                device.cmd_status(cmd, "error", stderr_list, self.cmd_validation_regex)

        self.cmd_results = device.commands