import asyncio
import aiohttp
import time
import json

async def main():
    async with aiohttp.ClientSession() as session:
        response = session.get()

if __name__ = "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() = start_time
