from deviceCommander import DeviceConfig
import yaml
import os

class configCommander():
    def __init__(self, config):
        self.new_config = config

    def find_validation(self):
        cwd = os.getcwd()
        with open(rf'{cwd}/device_yaml/device_yaml.yaml') as file:
            device_list = yaml.load(file, Loader=yaml.FullLoader)

        for device in device_list:
            if self.new_config['device']['device_type'] == device['device_type']:
                return device['regex_validation']
        return None

    def runConfig(self):
        validation_regex = self.find_validation()
        if ret is None:
            return "Failed to locate device validation regex"

        d = DeviceConfig(
            self.new_config['device']['hostname'],
            self.new_config['device']['username'],
            self.new_config['device']['password'],
            validation_regex)


        #cmd_list = ['config system interface\nedit port2\nset ip 192.168.51.0/24\nset allowaccess ping snmp http https\nend', 'show system interface port2']
        cmd_list = ['config system interface\nedit port2\nunset ip\nunset allowaccess\nend', 'show system interface port2']
        d.runCommands(cmd_list)
        return d.cmd_results



