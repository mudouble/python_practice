import threading
import time

def print_numbers():
    for i in range(5):
        print(threading.current_thread().name, ": ", i)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers())
thread2 = threading.Thread(target=print_numbers())

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main thread done")
