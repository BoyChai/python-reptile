'''
selenium模块
    - 它可以便捷获取网站中动态加载的数据
    - 便捷实现模拟登录
'''
import time

# 导入
from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建
chrome = webdriver.Chrome()
# 访问
chrome.get('https://www.taobao.com/')
# 执行js代码(滚动到底部)
chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
# 通过ID搜索q
search_input = chrome.find_element(By.ID, "q")
search_input.send_keys("悦克五代")
# 获取按钮
search_bt = chrome.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')
# 点击按钮
search_bt.click()
# 请求其他网址
chrome.get("https://www.baidu.com")
time.sleep(2)
# 回退
chrome.back()
time.sleep(2)
# 前进
chrome.forward()
time.sleep(2)
# 关闭
chrome.quit()
