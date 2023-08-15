import time

def order_coffe():
    print("Ordered Coffee")
    time.sleep(1)
    print("\t\t >> Received coffee")

def order_food():
    print("Ordered Food")
    time.sleep(5)
    print("\t\t >> Received Food")

def order_cake():
    print("Ordered Desert")
    time.sleep(3)
    print("\t\t >> Received Cake")
   
def main():
    order_coffe()
    order_food()
    order_cake() 

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"sync-operations executed in {elapsed:0.2f} seconds.")