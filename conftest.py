import pytest
import wda
from common import environment
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store"
    )


@pytest.fixture(scope="session", autouse=True)
def info(pytestconfig):
    info = environment.choose_env(pytestconfig.getoption('--env'))
    return info


def pytest_sessionfinish(session, exitstatus):
    # 测试结束时关闭app
    info = environment.choose_env(session.config.getoption('--env'))
    device=wda.Client(info.wda_address + ':' + info.wda_port)
    device.app_stop(info.bundle_id)