import time
from os import times
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class JDSpider:
    def __init__(self):
        # 使用的浏览器
        self.browser=webdriver.Edge()
    # 封装搜索方法
    def search(self,key):
        # self.browser.get(url)
        keyword = self.browser.find_element(By.ID, "key")
        # 4.输入搜索关键字
        keyword.send_keys(key)
        # 5.点搜索按钮或者回车键
        keyword.send_keys(Keys.ENTER)
        time.sleep(25)
    def getdata(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        divs = self.browser.find_elements(By.XPATH, "//div[@class='gl-i-wrap']")
        for div in divs:
            name = div.find_element(By.XPATH, "div/a/em").text
            print(name)
    def page(self):
        i=1
        # 找到下一页按钮
        while True:
            self.getdata()
            print("===========================================================")
            time.sleep(5)
            i += 2
            url="https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=63bb37230a7a41a2a7de520f023d939d&isList=0&page="+str(i)+"&s=56&click=0&log_id=1734600125026.7710"
            # 调用浏览器直接访问该页面
            self.browser.get(url)
            # self.browser.find_element(By.CLASS_NAME,"pn-next").click()
    def login(self,url,username,password):
        # 打开登录页面
        self.browser.get(url)
        # 找到用户名和密码输入框
        usernameinput=self.browser.find_element(By.ID, "loginname")
        passwordinput = self.browser.find_element(By.ID, "nloginpwd")
        # 输入用户名和密码
        usernameinput.send_keys(username)
        passwordinput.send_keys(password)
        # 点击登录按钮
        loginbtn=self.browser.find_element(By.ID,"loginsubmit")
        loginbtn.click()
        time.sleep(10)

spider=JDSpider()
spider.login("https://passport.jd.com/uc/login.aspx","17322461960","153759Zjn")
spider.search("手机")
# spider.getdata()
spider.page()