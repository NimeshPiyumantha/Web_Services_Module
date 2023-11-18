import asyncio

async def print_name(name):
    print(f"Name is {name}")

async def run():
    for i in range(100):
       await print_name(f"it-1-{i}")
       await asyncio.sleep(0.2)

async def run2():
    for i in range(100):
       await print_name(f"it-2-{i}")
       await asyncio.sleep(0.1)

async def main():
   await asyncio.gather(run(), run2())

asyncio.run(main())