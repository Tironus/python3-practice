class fortigate_config():
    def __init__(self, config):
        self.config = config

    def interface_config(self, params):
        params['interface'] = []
        for intf in self.config['device']['configuration']['interface']:
            intf_params = {
                "id": intf["id"],
                "ipv4_address": intf["ipv4_address"],
                "ipv4_prefix_len": intf["ipv4_prefix_len"],
                "allow_access": intf["allow_access"]
            }
            params['interface'].append(intf_params)
        return params

    def static_route_config(self, params):
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
        return params