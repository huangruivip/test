import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


# 获取cookie方法
def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookies, f)


class Testdemo:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    # # 复用
    # def test_wework():
    #     opt = webdriver.ChromeOptions()
    #     opt.debugger_address = "127.0.0.1:9222"
    #     driver = webdriver.Chrome(options=opt)
    #     driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     driver.find_element_by_id("menu_profile").click()
    #     time.sleep(10)
    #     driver.quit()

    # 使用cookie登陆
    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        with open("data.yaml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 点击添加成员
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("测试2")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("123456780")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("17621258523")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "保存").click()
