import time
from common.log import logger
from common.custom_operation import assert_element_exist


def back_to_homepage(device, bundle, retry_times=5):
    while retry_times:
        try:
            device.xpath(
                '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Image[2]').click(
                timeout=1)
        except Exception as e:
            pass
        logger.info("返回首页 尝试xpath")
        if assert_element_exist(device(label="骑行")): return True
        time.sleep(1)
        device.click(0.07, 0.083)  # 强行点坐标
        time.sleep(1)
        logger.info("返回首页 尝试坐标0.07, 0.083")
        if assert_element_exist(device(label="骑行")): return True
        retry_times -= 1
    restart_app(device, bundle)
    try:
        device(label="首页").click(timeout=1)
    except Exception as e:
        pass


def back_to_ride(device, bundle, retry_times=5):
    while retry_times:
        try:
            device(label="left arrow grey").click(timeout=1)
        except Exception as e:
            pass
        logger.info("返回ride 尝试left arrow grey")
        if assert_element_exist(device(label="助力车"), retry_times=3): return True
        try:
            device.xpath(
                '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[2]/Other[2]/Image[1]').click(
                timeout=1)
        except Exception as e:
            pass
        logger.info("返回ride 尝试xpath")
        if assert_element_exist(device(label="助力车"), retry_times=3): return True
        device.click(0.058, 0.082)
        logger.info("返回ride 尝试坐标0.058, 0.082")
        if assert_element_exist(device(label="助力车"), retry_times=3): return True
        device.click(0.044, 0.081)
        logger.info("返回ride 尝试坐标0.044, 0.081")
        if assert_element_exist(device(label="助力车"), retry_times=3): return True
        device.click(0.054, 0.079)
        logger.info("返回ride 尝试坐标0.054, 0.079")
        if assert_element_exist(device(label="助力车"), retry_times=3): return True
        retry_times -= 1
    restart_app(device, bundle)
    device(label="骑行").click(timeout=3)
    return False


def restart_app(device, bundle):
    device.app_stop(bundle)
    device.app_start(bundle)
