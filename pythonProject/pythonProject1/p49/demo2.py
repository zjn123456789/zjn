import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 1.打开浏览器（谷歌，ie）
browser=webdriver.Edge()
# 2.访问京东网站
browser.get("https://www.jd.com/")
# 3.定位输入框位置
keyword=browser.find_element(By.ID,"key")
# 4.输入搜索关键字
keyword.send_keys("手机")
# 5.点搜索按钮或者回车键
keyword.send_keys(Keys.ENTER)
time.sleep(20)
# 6.抓取数据
divs=browser.find_elements(By.XPATH,"//div[@class='gl-i-wrap']")
for div in divs:
    name=div.find_element(By.XPATH,"div/a/em").text
    print(name)
time.sleep(30)