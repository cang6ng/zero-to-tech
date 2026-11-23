import os
import threading

def worker():
    print("工作线程：")
    print("PID =", os.getpid())
    print("TID =", threading.get_native_id())

print("主线程：")
print("PID =", os.getpid())
print("TID =", threading.get_native_id())

t = threading.Thread(target=worker)
t.start()
t.join()
