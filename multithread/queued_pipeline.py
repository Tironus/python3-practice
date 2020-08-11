import time
import concurrent.futures
import random
import threading
import queue


class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def set_message(self, message):
        self.put(message)
        producer_pipeline.append(message)

    def get_message(self):
        message = self.get()
        consumer_pipeline.append(message)
        return message


def producer(pipeline, event):
    while not event.is_set():
        message = random.random()
        pipeline.set_message(message)
        print(f'producing message: {message}')


def consumer(pipeline, event):
    while not pipeline.empty() or not event.is_set():
        message = pipeline.get_message()
        print(f'consuming message {message}')
        time.sleep(message)


producer_pipeline = []
consumer_pipeline = []

if __name__ == '__main__':
    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.submit(producer, pipeline, event)
        e.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()
    print(producer_pipeline)
    print(consumer_pipeline)
