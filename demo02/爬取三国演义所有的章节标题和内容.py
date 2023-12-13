import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    # 爬取地址
    url="https://www.shicimingju.com/book/sanguoyanyi.html"
    # 设置请求头
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # 设置拼接地址的前缀
    prefix = "https://www.shicimingju.com"
    # 设置user-agent
    header = {
        'User-Agent': UA
    }
    # 使用 requests.get(url=url,headers=header).text 的话会出现乱码的问题
    # 获取每一章节的地址
    page_text = requests.get(url=url,headers=header).content
    soup = BeautifulSoup(page_text, 'lxml',)
    links = soup.select("#main_left > div > div.book-mulu > ul > li > a")
    # 写入的文件
    fp = open("./sanguo.txt",'w',encoding='utf-8')
    # 拿到每一章的请求地址和信息
    for v in links:
        # 获取每一章节的内容
        article_text = requests.get(url=prefix + v['href'], headers=header).content
        so = BeautifulSoup(article_text,'lxml')
        # 文章拼接并写入文件
        fp.write(v.text+":"+so.select_one("#main_left > div.card.bookmark-list").text+"\n")
        # 爬取成功之后输出标题
        print(v.text + " 已爬取成功")