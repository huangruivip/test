from typing import List

import pytest
import yaml
import os

from test_method.counter1 import counter_1


@pytest.fixture(scope='session')
def k():
    print("开始计算")
    yield
    print("计算结束")


@pytest.fixture(scope="class")
def get_calc1():
    print("获取计算机实例")
    calcc = counter_1()
    return calcc


# 获取yaml文件绝对路径
yaml_file_path = os.path.dirname(__file__) + "./cac.yaml"
with open(yaml_file_path, encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    myid = datas['add']['myid']
    div_datas = datas['div']['divss']
    divid = datas['div']['divid']
    sub_datas = datas['sub']['subb']
    sid_data = datas['sub']['subid']
    mul_data = datas['mul']['mulll']
    mid_data = datas['mul']['mullid']


@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas, ids=divid)
def get_add_datas1(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=sub_datas, ids=sid_data)
def get_add_datas2(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=mul_data, ids=mid_data)
def get_add_datas3(request):
    print("开始计算")
    data = request.param
    print(f"request.param 里面的数据是：{data}")
    yield data
    print("结束计算")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
