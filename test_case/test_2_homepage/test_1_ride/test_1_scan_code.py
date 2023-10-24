import time

import allure

from common.log import logger
from common.custom_operation import assert_element_exist
from common.attach_screenshot import attach_screenshot
from common.back_to_another_page import back_to_homepage,back_to_ride,restart_app

@allure.epic('[首页]模块')
@allure.feature('骑行页面-扫码相关功能验证')
class TestHomepageRideScanCode:
    
    @allure.title('验证骑行页面扫码功能')
    def test_homepage_ride_scan_code(self, info):
        device = info.device
        # 回到首页并截图
        try:
            device(label="首页").click(timeout=1)
        except Exception as e:
            logger.info("可能已在首页")
        attach_screenshot(device, '回到首页后截图')
        # 点击骑行按钮
        assert assert_element_exist(device(label="骑行"))
        device(label="骑行").click()
        attach_screenshot(device, '点击骑行按钮后截图')
        # 点击扫码开锁按钮
        assert assert_element_exist(device(label="扫码开锁"))
        device(label="扫码开锁").click()
        # 等待摄像头调起
        time.sleep(1)
        # 验证摄像头已调起
        assert assert_element_exist(device(label="对准二维码进行识别"))
        attach_screenshot(device, '点击扫码开锁按钮后截图')
        # 点击返回按钮
        back_to_ride(device, info.bundle_id)
        back_to_homepage(device, info.bundle_id)