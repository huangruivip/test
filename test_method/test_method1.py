import pytest
import yaml

from test_method.counter1 import counter_1

with open("./cac.yaml", encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    myid = datas['add']['myid']
    div_datas = datas['div']['divss']


class Testdome:

    def setup_class(self):
        self.cacl = counter_1()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,ab,",
        add_datas
        , ids=myid
    )
    def test_add(self, a, b, ab):
        # 调用add方法
        result = self.cacl.test_add(a, b)
        # 判断浮点数，做出处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果，断言
        assert result == ab

    @pytest.mark.parametrize(
        "d,e,de,",
        div_datas
    )
    def test_c(self, d, e, de):
        # 实例计算器类
        # 调用add方法
        result = self.cacl.test_divider(d, e)
        # 得到结果，断言
        assert result == de
