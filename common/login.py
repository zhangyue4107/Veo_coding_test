# 用于设备在未登录状态下登陆
import sys


from wda import Client
from common.log import logger
from common.custom_operation import assert_element_exist


def login(device: Client):
    device(label="我的").click()
    if assert_element_exist(device(label="张越")):
        logger.info("当前账号已经登录")
        return True
    try:
        device(label="login icon close").click(timeout=1)
        logger.info("自动跳转至登录页，已返回")
    except Exception as e:
        pass
    device(label="点击登录/注册").click(timeout=3)
    # 点击一键登录按钮
    device.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]').click(timeout=3)
    # 点击同意按钮
    device.xpath('//Window[1]/Other[3]/Other[1]/Other[1]/Other[1]/Button[2]/StaticText[1]').click(timeout=3)
    # 同意过后等待跳转
    if assert_element_exist(device(label="张越")):
        logger.info("登录成功")
        return True
    logger.error("登陆失败")
    sys.exit(1)
