import threading
import time
from threading import Lock

GLOBAL_VALUE = 0

LOCK = Lock()

def print_thread_name(name):
    print(f"Thread name is: thread - {name}")
    time.sleep(2)
    print(f"Thread - {name} is done")

def increment(name):
    global GLOBAL_VALUE, LOCK
    for _ in range(5_000_000):
        LOCK.acquire()
        GLOBAL_VALUE += 1
        LOCK.release()

thread_list = []
for index in range(6):
    thread_list.append(threading.Thread(target= increment, args= ((index, ))))
    thread_list[index].start()

for thread in thread_list:
    thread.join()

print(f"Global value = {GLOBAL_VALUE}")
