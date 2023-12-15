from lxml import etree

if __name__ == '__main__':
    # 导入本地页面
    tree = etree.parse('test.html',etree.HTMLParser())
    # 获取网页title
    # xpath的获取方式就是用/来 默认搜友标签都在/下 然后根据包含关系来确定
    # // 表示的是多个层级
    r= tree.xpath('/html/head/title')
    print(r)
    # 获取div
    # 返回body下的div
    r= tree.xpath('/html/body/div')
    print(r)
    # 在html下的所有div
    r= tree.xpath('/html//div')
    print(r)
    # 所有的div
    r= tree.xpath('//div')
    print(r)
    # 属性定位
    # @class指定class
    r = tree.xpath("//div[@class='song']")
    print(r)
    # 对应的div下的p标签
    r = tree.xpath("//div[@class='song']/p")
    print(r)
    # 第三个p标签
    r = tree.xpath("//div[@class='song']/p[3]")
    print(r)
    # 取文本
    # /text()
    r = tree.xpath("//div[@class='song']/p[3]/text()")[0]
    print(r)
    # 取属性值
    r = tree.xpath("//div[@class='song']/img/@src")[0]
    print(r)
