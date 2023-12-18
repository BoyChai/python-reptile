'''
高性能异步爬虫
目的：在爬虫中使用异步实现高性能的数据爬取操作。
异步爬虫的方式：
    - 多线程、多进程(不建议)：
        - 好处：可以为相关阻塞的操作单独开启线程或者进程，阻塞操作就可以异步执行。
        - 弊端：无法无限制的开启多线程或者多进程。
    - 线程池、进程池：
        - 好处：我们可以降低系统对进程或者进程创建和销毁的一个频率，从而很好的降低系统的开销。
        - 弊端：池中线程或进程的数量是有上线的。
'''
import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print("下载成功： ",str)
# 单线程
if __name__ == '__danxiancheng__':
    name_list = ['xiaozi', 'aa', 'bb', 'cc']

    start_time = time.time()
    for i in range(len(name_list)):
        get_page(name_list[i])
    end_time = time.time()
    print("%d second" % (end_time - start_time))
# 线程池
if __name__ == '__main__':
    start_time = time.time()

    name_list = ['xiaozi', 'aa', 'bb', 'cc']
    # 实例一个线程池对象
    pool=Pool(4)
    # 将列表中每一个表示元素传递给get_page机械能处理
    pool.map(get_page,name_list)
    end_time = time.time()
    print("%d second" % (end_time - start_time))
