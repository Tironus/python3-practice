from configCommander import configCommander
from commandGenerator import commandGenerator

payload = {
    "device": {
        "hostname": "192.168.20.8",
        "username": "admin",
        "password": "admin",
        "device_type": "fortigate",
        "firmware_version": "5.6.4",
        "configuration": {
            "interface": [
                {
                    "id": "port5",
                    "ipv4_address": "192.168.52.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        " ping",
                        " ssh",
                        " http",
                        " https",
                        " snmp"
                    ]
                },
                {
                    "id": "port6",
                    "ipv4_address": "192.168.72.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        " ping",
                        " ssh",
                        " http",
                        " snmp"
                    ]
                },
                {
                    "id": "port7",
                    "ipv4_address": "192.168.74.43",
                    "ipv4_prefix_len": "24",
                    "allow_access": [
                        " ping"
                    ]
                }
            ],
            "static_route": [
                {
                    "id": "100",
                    "dst_ip": "10.10.10.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
                },
                {
                    "id": "101",
                    "dst_ip": "10.10.11.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
                },
                {
                    "id": "102",
                    "dst_ip": "10.10.12.0",
                    "dst_prefix_len": "24",
                    "device": "port5",
                    "gateway": "192.168.52.44"
                }
            ]
        }
    }
}

test_api = {
  "device": {
    "hostname": "192.168.20.8",
    "username": "admin",
    "password": "admin",
    "device_type": "fortigate",
    "firmware_version": "5.6.4",
    "configuration": {
      "id": "500",
      "dst_ip": "50.50.50.0",
      "dst_prefix_len": "24",
      "device": [
        "port2"
      ],
      "gateway": "192.168.52.44"
    }
  }
}

c = configCommander(payload)
ret, status, msg = c.runConfig()


print(f'COMMAND RESULTS: {status}')
print(f'msg: {msg}')
print('=================================')
print('=================================\n')
for result in ret:
    print(f'command: {result}')
    print(f'command submitted: {ret[result]["submit_config_result"]}')
    print(f'command result: {ret[result]["device_accepted_result"]}\n')
    print(f'{ret[result]["device_output"]}')
    print('=================================')
    print('=================================\n')