import time
import threading

def my_func1(name):
    print(f"thread_2 started with {name}\n")
    time.sleep(10)
    print("thread_2 ended\n")


def my_func2(name):
    print(f"thread_3 started with {name}\n")
    time.sleep(10)
    print("thread_3 ended\n")


def my_func3(name):
    print(f"thread_4 started with {name}\n")
    time.sleep(10)
    print("thread_4 ended\n")

if __name__ == "__main__":
    print("thread_1 started\n")
    # daemon=True to run thread in background will be killed when main thread is finished if work is not completed
    # t = threading.Thread(target=my_func, args=["my_arg"], daemon=True)
    t1 = threading.Thread(target=my_func1, args=["my_arg1"])
    t1.start()
    t2 = threading.Thread(target=my_func2, args=["my_arg2"])
    t2.start()
    t3 = threading.Thread(target=my_func3, args=["my_arg3"])
    t3.start()
    # joins main thread with second thread and will wait until second thread completes before completing main thread.
    t1.join()
    t2.join()
    t3.join()
    print("thread_1 ended\n")