from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List

class DeviceConfig(BaseModel):
    device: Dict
    hostname: str
    username: str
    password: str
    device_type: str
    firmware_version: str
    configuration: Dict
    interface: List[Dict]



app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}