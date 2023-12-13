import requests
if __name__ == "__main__":
    # 请求地址
    url="https://image.boychai.xyz/article/Kubernetes_pod_24.png"

    # 发起请求
    # content返回的是二进制形式的图片数据
    # text(字符串) content(二进制) json() (json数据)
    img_data = requests.get(url=url).content

    # wb是二进制写入模式
    with open("img.png",'wb') as fp:
        fp.write(img_data)