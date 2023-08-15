import concurrent.futures
from time import sleep

def download(filename, size):
    for i in range (0, size):
        print(f"{filename} downlaoded {i} MB")
        sleep(1)

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(download, "pictures.zip", 5)
pool.submit(download, "musiz.zip", 10)

pool.shutdown(wait=True)