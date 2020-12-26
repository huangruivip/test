from time import sleep

from selenium.webdriver.common.by import By

from test_4.sele_po.page.basepage import BasePage


class addresspage(BasePage):
    # 添加成员
    def click_adda(self):
        from test_4.sele_po.page.adda import Add
        self.find(By.LINK_TEXT, "添加成员").click()
        return Add(self.driver)

    def click_ab(self):
        from test_4.sele_po.page.adda import Add
        self.find(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div").click()
        return Add(self.driver)

    def add_dy(self):
        ele = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in ele:
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        return name_list
