import asyncio

async def request(url):
    print('正在请求的url是：',url)
    print('请求成功',url)

# 被async修饰的函数，调用之后返回的是一个协程对象
c = request('baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 把协程对象注册到loop中，之后启动loop
# loop.run_until_complete(c)
# task使用
# loop = asyncio.get_event_loop()
# # 创建一个taks
# task = loop.create_task(c)
# print(task)
# # 启动任务
# loop.run_until_complete(task)
# print(task)
# future的使用
# loop = asyncio.get_event_loop()
# future = asyncio.ensure_future(c)
# print(future)
# loop.run_until_complete(future)
# print(future)
# 回调函数
def callbak_func(task):
    print(task.result())
# 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# ji昂回调函数绑定到任务对象中
task.add_done_callback(callbak_func)
loop.run_until_complete(task)
