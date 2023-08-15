import time
import asyncio

async def order_coffe():
    print("Ordered Coffee")
    await asyncio.sleep(1)
    print("\t\t >> Received coffee")

async def order_food():
    print("Ordered Food")
    await asyncio.sleep(5)
    print("\t\t >> Received Food")

async def order_cake():
    print("Ordered Desert")
    await asyncio.sleep(3)
    print("\t\t >> Received Cake")
   
async def main():
    await asyncio.gather(order_coffe(), order_food(), order_cake())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"sync-operations executed in {elapsed:0.2f} seconds.")