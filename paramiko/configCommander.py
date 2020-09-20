from deviceCommander import DeviceConfig
from commandGenerator import commandGenerator
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
        if validation_regex is None:
            return "Failed to locate device validation regex"

        d = DeviceConfig(
            self.new_config['device']['hostname'],
            self.new_config['device']['username'],
            self.new_config['device']['password'],
            validation_regex)

        cg = commandGenerator(self.new_config, 'configure')
        cmds = cg.generateCommands()
        d.runCommands(cmds)
        for result in d.cmd_results:
            if d.cmd_results[result]['submit_config_result'] != 'success' or d.cmd_results[result]['device_accepted_result'] != 'success':
                print('failure detected, backing out config...')
                cg.update_config_type('backout')
                cmds = cg.generateCommands()
                d.runCommands(cmds)
                print('backout complete')
        return d.cmd_results



