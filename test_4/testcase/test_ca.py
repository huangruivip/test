import pytest

from test_4.sele_po.page.home import homepage


class TestLogin:
    def setup(self):
        # 实例化首页
        self.main = homepage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,phone", [("测试1", "1111", "17656556666")])
    def test_login(self, name, id, phone):
        # 调用链，点击首页，点击通讯录，添加成员，返回通讯录断言
        name_list = self.main.goto_address().click_adda() \
            .input_s(name, id, phone).add_dy()
        print(name_list)
        assert name in name_list

    @pytest.mark.parametrize("name,id,phone", [("测试2", "1121", "17655556666")])
    def test_logins(self, name, id, phone):
        name_list = self.main.goto_add().click_ab() \
            .input_s(name, id, phone).add_dy()
        print(name_list)
        assert name in name_list
