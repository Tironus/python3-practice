import time
import concurrent.futures
import random

LAST_MSG = 'LAST_MSG'

class Pipeline():
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None

    def set_message(self, message):
        self.message = message

    def get_message(self):
        message = self.message
        return message

def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randrange(1, 10)
        pipeline.set_message(message)
        producer_pipeline.append(message)
        print(f'producing message: {message}')
    pipeline.set_message('LAST_MSG')

def consumer(pipeline):
    while pipeline.message is not LAST_MSG:
        print(f'consuming message {pipeline.message}')
        message = pipeline.get_message()
        time.sleep(message)
        consumer_pipeline.append(message)


producer_pipeline = []
consumer_pipeline = []

if __name__ == '__main__':
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.submit(producer, pipeline)
        e.submit(consumer, pipeline)

    print(producer_pipeline)
    print(consumer_pipeline)