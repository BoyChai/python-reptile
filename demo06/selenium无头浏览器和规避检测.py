'''
无头浏览器其实就说放在后台运行(无可视化界面)
'''
import time

from selenium import webdriver

# 导入对应的类
from selenium.webdriver import ChromeOptions

# 实例化一个Options对象，用来控制chrome以无界面模式打开
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])

# 规避检测
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://www.baidu.com")
print(chrome.page_source)
