from configCommander import configCommander

payload = {
    "device": {
        "hostname": "172.16.233.130",
        "username": "admin",
        "password": "admin",
        "device_type": "fortigate",
        "firmware_version": "5.6.4",
        "configuration": {
            "interface": [
                {
                    "id": "port2",
                    "ipv4_address": "192.168.52.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        "ping",
                        "ssh",
                        "http",
                        "https",
                        "snmp"
                    ]
                }
            ],
            "static_route": [
                {
                    "id": "100",
                    "dst_ip": "10.10.10.0",
                    "dst_prefix_len": "24",
                    "device": "port2"
                }
            ]
        }
    }
}

c = configCommander(payload)
ret = c.find_validation()
print(ret)



#print('COMMAND RESULTS:')
#print('=================================')
#print('=================================\n')
#for result in d.cmd_results:
#    print(f'command: {result}')
#    print(f'command submitted: {d.cmd_results[result]["submit_config_result"]}')
#    print(f'command result: {d.cmd_results[result]["device_accepted_result"]}\n')
#    print(f'{d.cmd_results[result]["device_output"]}')
#    print('=================================')
#    print('=================================\n')