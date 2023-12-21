# 导入
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入动作链对应的类
from selenium.webdriver import ActionChains
chrome = webdriver.Chrome()
chrome.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

# 如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
# 切换浏览器定位的作用域
chrome.switch_to.frame('iframeResult')
div = chrome.find_element(By.ID, 'draggable')
# 实例动作链
action = ActionChains(chrome)
# 点击且长按div
action.click_and_hold(div)

# 向右慢慢拖动
for i in range(100):
    # perform()立即执行动作链操作，这个是拖动17像素
    # 注意x和y参数，第一个是x水平方向，y是垂直方向
    action.move_by_offset(i,0).perform()
    time.sleep(0.2)

# 释放动作链
action.release()
time.sleep(2)