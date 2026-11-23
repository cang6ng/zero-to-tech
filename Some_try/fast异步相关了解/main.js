
const { threadId } = require("node:worker_threads");

function searchTool(name) {
  console.log(`开始: ${name}, 线程: ${threadId}`);

  return new Promise(resolve => {
    setTimeout(() => {
      console.log(`完成: ${name}, 线程: ${threadId}`);
      resolve(`${name} 搜索结果`);
    }, 1000);
  });
}

async function main() {
  console.log("进程 PID:", process.pid);

  const results = await Promise.all([
    searchTool("GraphRAG"),
    searchTool("HippoRAG"),
    searchTool("LightRAG")
  ]);

  console.log(results);
}

main().catch(console.error);
