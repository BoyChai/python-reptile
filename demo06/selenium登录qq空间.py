import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://i.qq.com/")

chrome.switch_to.frame('login_frame')
bt1 = chrome.find_element(By.ID,'switcher_plogin')
bt1.click()

username = chrome.find_element(By.ID, 'u')
password = chrome.find_element(By.ID, 'p')
username.send_keys("1972567225")
password.send_keys("nn86830677")
bt2 = chrome.find_element(By.XPATH,'//*[@id="login_button"]')

bt2.click()
time.sleep(1000)