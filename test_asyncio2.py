import asyncio

counter = 0

async def increment():
    global counter

    old_value = counter
    await asyncio.sleep(0)
    counter = old_value + 1

async def main():
    await asyncio.gather(
        increment(),
        increment()
    )
    print(counter)

asyncio.run(main())
