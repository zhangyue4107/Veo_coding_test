import sys

import attr
import wda

from common.login import login

@attr.s()
class Dev:
    """
    wda启动时使用tidevice
    1.安装tidevice
    pip3 install --upgrade tidevice
    2.安装WebDriverAgent
    3.启动WebDriverAgent
    tidevice -u {测试设备的id用tidevice list 查看} wdaproxy -B com.facebook.WebDriverAgentRunnerZhangy.xctrunner --port 8200
    """
    wda_address = 'http://127.0.0.1'
    wda_port = '8200'
    # app基础配置
    # app bundle id
    bundle_id = 'com.jingyao.EasyBike'
    # 账户基本信息设置
    phone_number = '15884473327'
    user_name = '张越'
    try:
        device = wda.Client(wda_address + ':' + wda_port)
        device_info = attr.ib(default=device.info)
        assert device_info is not None
    except Exception as e:
        print('wda启动失败,reason:{}'.format(e))
        sys.exit(1)
    try:
        # app启动
        device.app_stop(bundle_id)
        device.app_start(bundle_id)
    except Exception as e:
        print('app启动失败,reason:{}'.format(e))
        sys.exit(1)
    # 设备登录
    try:
        login(device, user_name)
    except Exception as e:
        print('登录失败,reason:{}'.format(e))
        sys.exit(1)

@attr.s
class Test(Dev):
    # 做环境区分预留
    pass


def choose_env(env):
    if env == 'dev':
        return Dev()
    if env == 'test':
        return Test()

