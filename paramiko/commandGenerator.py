import os
from jinja2 import Environment, FileSystemLoader

class commandGenerator():
    def __init__(self, config, config_type):
        self.config = config
        self.config_type = config_type
        self.commands = []

    def fortigate(self, template):
        params = {}
        command_list = []
        if self.config['device']['configuration']['interface']:
            for intf in self.config['device']['configuration']['interface']:
                params["id"] = intf["id"]
                params["ipv4_address"] = intf["ipv4_address"]
                params["ipv4_prefix_len"] = intf["ipv4_prefix_len"]
                params["allow_access"] = intf["allow_access"]

                output = template.render(params=params)
                command_list.append(output)
        self.commands = command_list

    def generateCommands(self):
        cwd = os.getcwd()
        template_path = f"{cwd}/command_templates"
        template_name = f"{self.config['device']['device_type']}_commands.txt"

        file_loader = FileSystemLoader(template_path)
        env = Environment(loader=file_loader)
        template = env.get_template(template_name)

        if self.config['device']['device_type'] == 'fortigate':
            self.fortigate(template)

        return self.commands

