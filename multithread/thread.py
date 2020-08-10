# cpu - hardware that executes code
# os - schedules work for the cpu
# process - program as it is being executed
# thread - part of a process
import time
import threading

def my_func(name):
    print(f"thread_2 started with {name}\n")
    time.sleep(10)
    print("thread_2 ended\n")

if __name__ == "__main__":
    print("thread_1 started\n")
    t = threading.Thread(target=my_func, args=["my_arg"])
    t.start()
    print("thread_1 ended\n")