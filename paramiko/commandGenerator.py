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
        if 'interface' in self.config['device']['configuration']:
            params['interface'] = []
            for intf in self.config['device']['configuration']['interface']:
                intf_params = {
                    "id": intf["id"],
                    "ipv4_address": intf["ipv4_address"],
                    "ipv4_prefix_len": intf["ipv4_prefix_len"],
                    "allow_access": intf["allow_access"]
                }
                params['interface'].append(intf_params)

        if 'static_route' in self.config['device']['configuration']:
            params['static_route'] = []
            for sr in self.config['device']['configuration']['static_route']:
                route_params = {
                    "id": sr["id"],
                    "dst_ip": sr["dst_ip"],
                    "dst_prefix_len": sr["dst_prefix_len"],
                    "device": sr["device"],
                    "gateway": sr["gateway"]
                }
                params['static_route'].append(route_params)

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

