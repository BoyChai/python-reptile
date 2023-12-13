import requests
# 正则模块
import re
# 爬取文章的图片
if __name__=="__main__":
    url="https://blog.boychai.xyz/index.php/archives/31/"
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    header = {
        'User-Agent':UA
    }

    # 拿到整张页面的源码数据
    page_data = requests.get(url=url,headers=header).text
    # 解析出所有页面中的图片

    # 这里写的正则有问题，然后具体流程是 爬到连接之后 挨个通过图片爬取那个py来做一个遍历处理即可拿到图片
    '''
    <img src="https://image.boychai.xyz/article/Kubernetes_pod_23.png" alt="客户端" title="客户端" style="" class="block">
    <img src="(.*?)" alt="客户端" title="客户端" style="" class="block">
    <a class="light-link" data-fancybox="gallery" no-pjax="" data-type="image" data-caption="请求流程" href="https://image.boychai.xyz/article/Kubernetes_pod_24.png"><img src="https://image.boychai.xyz/article/Kubernetes_pod_24.png" alt="请求流程" title="请求流程" style="" class="block"><figcaption class="post-img-figcaption">请求流程</figcaption></a>
    <a class="light-link" data-fancybox="gallery" no-pjax="" data-type="image" data-caption="(.*?)" href="(.*?)"><img
    '''
    ex = '<a class="light-link" data-fancybox="gallery" no-pjax="" data-type="image" data-caption="(.*?)" href="(.*?)"><img'
    imgList = re.findall(ex,page_data,re.S)
    print(imgList)