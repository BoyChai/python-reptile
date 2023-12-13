import requests
import lxml
from bs4 import BeautifulSoup
# 使用bs4来做数据解析
# bs4的解析是使用标签定位
# 提取标签、标签属性中存储的数据值

if __name__ == '__main__':
    # 本地
    fp = open("test.html",'r',encoding="utf-8")
    soup = BeautifulSoup(fp,'lxml')
    # 网络
    # page_text = requests.get("").text
    # soup = BeautifulSoup(fp, 'lxml')

    # 拿到内容中的第一个a标签
    print("拿到内容中的第一个a标签")
    print(soup.a)
    print("第二种方式")
    print(soup.find("a"))

    # 属性定位
    print("属性定位拿标签")
    # 切记class要跟class_
    print(soup.find("div",class_="song"))

    # 上面的find都是搜索第一个find_all是搜索列表 所有符合标准的
    # find_all返回的是列表
    print("搜索列表")
    a_all = soup.find_all("a")
    for v in a_all:
        print(v)

    # select 选择器
    # 直接使用select方法返回的是列表，select_one是单个
    print("选择器 select")
    print(soup.select('body > div.tang > ul > li:nth-child(6) > b'))
    print(soup.select_one('body > div.tang > ul > li:nth-child(6) > b'))
    # 获取对应的文本内容的三种方式
    print(soup.select_one('body > div.tang > ul > li:nth-child(6) > b').get_text())
    print(soup.select_one('body > div.tang > ul > li:nth-child(6) > b').text)
    print(soup.select_one('body > div.tang > ul > li:nth-child(6) > b').string)

    # 获取属性值
    print("获取a标签的属性值")
    a_all = soup.find_all("a")
    for v in a_all:
        print(v['href'])


