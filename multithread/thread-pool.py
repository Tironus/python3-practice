# cpu - hardware that executes code
# os - schedules work for the cpu
# process - program as it is being executed
# thread - part of a process
import time
import random
import concurrent.futures
import threading

number_of_threads = 0

def my_func(name):
    global number_of_threads
    number_of_threads += 1
    thread_id = threading.current_thread().ident
    print(f"thread_{thread_id} started with {name}\n")
    time.sleep(random.randrange(3, 7, 2))
    print(f"thread_{thread_id} ended\n")
    number_of_threads -= 1

if __name__ == "__main__":
    number_of_threads += 1
    print(f"thread_{threading.current_thread().ident} started\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(my_func, ['arg_1', 'arg_2', 'arg_3'])
    print(f"thread_{threading.current_thread().ident} ended\n")