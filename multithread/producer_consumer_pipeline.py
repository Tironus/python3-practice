import time
import concurrent.futures
import random
import threading

LAST_MSG = 'LAST_MSG'


class Pipeline():
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def set_message(self, message):
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()

    def get_message(self):
        self.producer_lock.release()
        message = self.message
        self.consumer_lock.acquire()
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