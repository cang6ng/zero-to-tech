import asyncio

async def search_paper(topic):
    await asyncio.sleep(1)  # 模拟网络请求
    return f"{topic} 的搜索结果"

async def main():
    topics = ["GraphRAG", "HippoRAG", "LightRAG"]

    # 三个搜索任务并发执行
    results = await asyncio.gather(
        *(search_paper(topic) for topic in topics)
    )

    # 三个任务结束后，统一处理结果
    for result in results:
        print(result)

asyncio.run(main())
