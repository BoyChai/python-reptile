import os
from multiprocessing.dummy import Pool

import requests
from lxml import etree


header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
def getVideo(id):
    url1 = "https://www.pearvideo.com/videoStatus.jsp?contId=" + id
    url = "https://www.pearvideo.com/video_"+id
    h = header
    h["Referer"]=url
    data = requests.get(url=url1, headers=h).json()
    video_image = data['videoInfo']['video_image']
    srcUrl = data['videoInfo']['videos']['srcUrl']
    key = video_image.split('/')[5].split('-')[0]+"-"+video_image.split('/')[5].split('-')[1]
    return srcUrl.replace(srcUrl.split('/')[6].split('-')[0],key)

def saveVideo(dic):
    print("正在下载 "+dic['name'])
    videoData = requests.get(url=dic['url'], headers=header).content
    if not os.path.exists("./videoLibs"):
        os.mkdir("./videoLibs")
    with open("./videoLibs/"+dic['name']+".mp4",'wb') as fp:
        fp.write(videoData)
        print(dic['name']+" 下载完成")

if __name__ == '__main__':
    urls = []
    url = "https://www.pearvideo.com/category_1"
    # 线程池处理的是阻塞且耗时的操作
    page_data=requests.get(url=url,headers=header).text
    tree = etree.HTML(page_data)
    videos = tree.xpath('//div[@id="listvideoList"]//li[@class="categoryem "]')
    for video in videos:
        id= str(video.xpath('.//a[@class="vervideo-lilink actplay"]/@href')[0]).split("_")[1]
        name = video.xpath('.//div[@class="vervideo-title"]/text()')[0]
        video_url = getVideo(id)
        dic = {
            'name':name,
            'url':video_url
        }
        urls.append(dic)
    # 创建三个线程池
    pool = Pool(3)
    # 执行任务
    pool.map(saveVideo, urls)
    # 关闭进程池，表示不再接受新的任务
    pool.close()
    # 等待所有任务完成，会阻塞
    pool.join()
