import asyncio
import time

start = time.time()
async def request(url):
    print('正在下载',url)
    time.sleep(2)
    print('下载完毕',url)
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com',
]
# 人物列表：存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
# 运行
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stasks))
end = time.time()

print(start-end)