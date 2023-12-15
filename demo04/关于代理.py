'''
代理：破解封ip的这种反爬机制
代理的作用：
    - 突破自身IP访问的限制
    - 隐藏自身真实IP
代理相关的网站：
    - 快代理 https://www.kuaidaili.com/
    - 巨量IP https://tg.juliangdaili.com/api
代理的透明度：
    - 透明：服务端知道该次请求使用了代理，并且也知道对应的真实ip
    - 匿名：服务端知道使用了代理，不知道真实ip
    - 高匿：服务端不知道使用了代理，更不知道真实的ip
'''
import requests
from lxml import etree
if __name__ == '__main__':
    url = "https://ip.900cha.com/"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # 设置user-agent
    header = {
        'User-Agent': UA
    }
    page_text = requests.get(url=url, headers=header, proxies={"https": "127.0.0.1:10811"}).text
    tree = etree.HTML(page_text)
    ip = tree.xpath("/html/body/div/div/div/div[1]/div[1]/ul/li[3]/text()")
    print(str(ip).replace(" ","").replace("\\n",""))