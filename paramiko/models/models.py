import enum
from pydantic import BaseModel
from typing import Dict, List, Optional


class AllowAccess(enum.Enum):
    ssh = '1'
    http = '2'
    https = '3'
    snmp = '4'

class DevicePorts(enum.Enum):
    port1 = 'port1'
    port2 = 'port2'
    port3 = 'port3'
    port4 = 'port4'


class InterfaceValues(BaseModel):
    id: str
    ipv4_address: str
    ipv4_prefix_len: int
    allow_access: List[AllowAccess]

class StaticRouteValues(BaseModel):
    id: str
    dst_ip: str
    dst_prefix_len: str
    device: List[DevicePorts]
    gateway: str

class ConfigInteface(BaseModel):
    hostname: str
    username: str
    password: str
    device_type: str
    firmware_version: str
    configuration: Optional[InterfaceValues]

class ConfigRoutes(BaseModel):
    hostname: str
    username: str
    password: str
    device_type: str
    firmware_version: str
    configuration: Optional[StaticRouteValues]

class ConfigDeviceInterface(BaseModel):
    device: Optional[ConfigInteface]

class ConfigDeviceRoute(BaseModel):
    device: Optional[ConfigRoutes]

class ConfigResponse(BaseModel):
    restults: List
    status: str
    msg: str