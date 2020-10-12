import os
from jinja2 import Environment, FileSystemLoader
from config_params import fortigate_config_params

class commandGenerator():
    def __init__(self, config, config_type):
        self.config = config
        self.config_type = config_type
        self.commands = []

    def update_config_type(self, config_type):
        self.config_type = config_type

    def config_fortigate(self, template):
        params = {}
        command_list = []

        cp = fortigate_config_params.fortigate_config(self.config)
        if 'interface' in self.config['device']['configuration']:
            params = cp.interface_config(params)

        if 'static_route' in self.config['device']['configuration']:
            params = cp.static_route_config(params)

        output = template.render(params=params)
        command_list.append(output)
        self.commands = command_list

    def generateCommands(self):
        home_env = os.getenv("HOME")
        if self.config_type == 'configure':
            template_path = f"{home_env}/python3-practice/python3-practice/paramiko/command_templates/config"
            template_name = f"{self.config['device']['device_type']}_commands.txt"
        elif self.config_type == 'backout':
            template_path = f"{home_env}/python3-practice/python3-practice/paramiko/command_templates/backout"
            template_name = f"{self.config['device']['device_type']}_backout_commands.txt"
        else:
            print(f'invalid config type: {self.config_type}')

        file_loader = FileSystemLoader(template_path)
        env = Environment(loader=file_loader)
        template = env.get_template(template_name)

        if self.config['device']['device_type'] == 'fortigate':
            self.config_fortigate(template)

        return self.commands

