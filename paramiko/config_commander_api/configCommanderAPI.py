import sys
sys.path.insert(1, '/Users/tgionfriddo/PycharmProjects/python3-practice/paramiko/config_commander_api')
sys.path.insert(2, '/Users/tgionfriddo/PycharmProjects/python3-practice/paramiko/models')
sys.path.insert(3, '/Users/tgionfriddo/PycharmProjects/python3-practice/paramiko')

import models
from configCommander import configCommander
from fastapi import FastAPI

app = FastAPI()

@app.post("/config_interface", response_model=models.ConfigResponse)
async def post_config(config_data: models.ConfigDeviceInterface):
    c = configCommander(payload)
    results, status, msg = c.runConfig()
    return results

@app.post("/config_static_routes", response_model=models.ConfigResponse)
async def post_config(config_data: models.ConfigRoutes):
    c = configCommander(payload)
    results, status, msg = c.runConfig()
    return results