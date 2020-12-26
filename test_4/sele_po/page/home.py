from selenium.webdriver.common.by import By

from test_4.sele_po.page.address import addresspage
from test_4.sele_po.page.basepage import BasePage


class homepage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 点击通讯录
    def goto_address(self):
        self.find(By.ID, "menu_contacts").click()

        return addresspage(self.driver)

    def goto_add(self):
        self.find(By.ID, "menu_index").click()
        return addresspage(self.driver)
