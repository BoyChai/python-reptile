'''
默认使用requests库进行请求的时候每次都是新的请求，在某些网页可能设置了用户等功能 只有登录之后才可以获取某些内容
这个时候就不能通过直接使用request来发送请求了得用session进行请求创建方法如下
他的作用就是会把某些信息存储到session中下次请求的时候会持久化在这个请求中，对应的一些认证信息也会存储在session里
'''
import requests
if __name__ == '__main__':
    session = requests.Session()
