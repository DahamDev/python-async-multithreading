import threading
from time import sleep

def download(filename, size):
    for i in range (0, size):
        print(f"{filename} downlaoded {i} MB")
        sleep(1)

thread1 = threading.Thread(target=download, args=("pictures.zip", 5))
thread2 = threading.Thread(target=download, args=("musiz.zip", 10))

thread1.start()
thread2.start()