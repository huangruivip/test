from time import sleep

from test_4.sele_po.page.address import addresspage

from selenium.webdriver.common.by import By

from test_4.sele_po.page.basepage import BasePage


class Add(BasePage):
    _s_name = (By.ID, "username")
    _s_id = (By.ID, "memberAdd_acctid")
    _s_phone = (By.ID, "memberAdd_phone")

    def input_s(self, name, id, phone):
        self.find(*self._s_name).click()
        self.find(*self._s_name).send_keys(name)
        self.find(*self._s_id).send_keys(id)
        self.find(*self._s_phone).send_keys(phone)
        self.find(By.LINK_TEXT, "保存").click()
        sleep(5)
        return addresspage(self.driver)
