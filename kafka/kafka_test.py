from aiokafka import AIOKafkaProducer
from aiokafka import AIOKafkaConsumer

import asyncio

loop = asyncio.get_event_loop()

async def send_one():
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers='worker.tonykube.net:31071', api_version=('2.6.0'))
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        for _ in range(10):
            msg = f"Test Msg {_}"
            msg = str.encode(msg)
            await producer.send_and_wait("my_topic", msg)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

loop.run_until_complete(send_one())