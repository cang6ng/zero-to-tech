import asyncio
import time

async def call_llm3(user):
    print(f"{user} 开始请求")
    await asyncio.sleep(3)  # 模拟异步等待 LLM
    print(f"{user} 收到回复")

async def call_llm4(user):
    print(f"{user} 开始请求")
    await asyncio.sleep(4)  # 模拟异步等待 LLM
    print(f"{user} 收到回复")

async def main():
    start = time.perf_counter()

    await asyncio.gather(
        call_llm4("用户 A"),
        call_llm3("用户 B")
    )

    print(f"总耗时: {time.perf_counter() - start:.1f} 秒")

asyncio.run(main())
