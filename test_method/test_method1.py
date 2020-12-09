import allure
import pytest
import yaml

from test_method.counter1 import counter_1


@allure.feature("测试计算器")
class Testdome:
    @pytest.mark.add
    @pytest.mark.run(order=1)
    @allure.story("测试加法")
    def test_add(self, get_calc1, get_add_datas):
        result = None
        try:
            # 调用add方法
            with allure.step("计算俩个数相加的值"):
                result = get_calc1.test_add(get_add_datas[0], get_add_datas[1])
            # 判断浮点数，做出处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
            # 得到结果，断言
        assert result == get_add_datas[2]

    @pytest.mark.div
    @pytest.mark.run(order=4)
    @allure.story("测试除法")
    def test_div(self, get_calc1, get_add_datas1):
        # 实例计算器类
        # 调用add方法
        result = None
        try:
            with allure.step("计算俩个数相除的值"):
                result = get_calc1.test_divider(get_add_datas1[0], get_add_datas1[1])
        # 得到结果，断言
        except Exception as e:
            print(e)
        assert result == get_add_datas1[2]

    @pytest.mark.sub
    @pytest.mark.run(order=3)
    @allure.story("测试减法")
    def test_d(self, get_calc1, get_add_datas2):
        # 实例计算器类
        # 调用add方法
        with allure.step("计算俩个数相减的值"):
            result = get_calc1.test_sub(get_add_datas2[0], get_add_datas2[1])
        # 得到结果，断言
        assert result == get_add_datas2[2]

    @pytest.mark.mul
    @pytest.mark.run(order=3)
    @allure.story("测试乘法")
    def test_e(self, get_calc1, get_add_datas3):
        # 实例计算器类
        # 调用add方法
        with allure.step("计算俩个数相乘的值"):
            result = get_calc1.test_mull(get_add_datas3[0], get_add_datas3[1])
        # 得到结果，断言
        assert result == get_add_datas3[2]
