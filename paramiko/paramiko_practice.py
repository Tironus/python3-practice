import paramiko
import pprint

class cmd_object():
    def __init__(self, hostname):
        self.hostname = hostname
        self.commands = {}

    def cmd_status(self, cmd, result, output):
        self.commands[cmd] = {
                                "result": result,
                                "device_output": output
                             }

pp = pprint.PrettyPrinter(indent=4)
cmd_list = ['get system status', 'get router info routing-table all', 'get system interface']

test = paramiko.SSHClient()
test.set_missing_host_key_policy(paramiko.AutoAddPolicy())
test.connect(hostname="172.16.233.130", username='admin', password='admin', look_for_keys=False)


device = cmd_object("172.16.233.130")
for cmd in cmd_list:
    stdin, stdout, stderr = test.exec_command(cmd)
    stdin = stdin.channel.makefile_stdin()
    stderr = stderr.channel.makefile_stderr()

    stdin_list = [line for line in stdin.readlines()]
    stderr_list = [line for line in stderr.readlines()]

    if len(stdin_list) > 0:
        device.cmd_status(cmd, "success", stdin_list)

    if len(stderr_list) > 0:
        device.cmd_status(cmd, "error", stderr_list)


pp.pprint(device.commands)