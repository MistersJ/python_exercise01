# -*- coding: UTF-8 -*-
# @Author: Lwx634423
# @Date: 2020/12/21

from os import environ as env

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store", default="http://cqp.kweweb.huawei.com", help="the testcase run environment."
    )


@pytest.fixture(scope="session", autouse=True)
def host(request):
    # define an environment varible for the testcase.
    env["host"] = request.config.getoption("--cmdhost")
