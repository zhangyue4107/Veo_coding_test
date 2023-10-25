import time

import allure

from common.log import logger
from common.custom_operation import assert_element_exist
from common.attach_screenshot import attach_screenshot
from common.back_to_another_page import back_to_homepage,back_to_ride,restart_app

@allure.epic('[首页]模块')
@allure.feature('骑行页面-地图相关功能验证')
class TestHomepageRideMap:
    @allure.title('验证骑行页面地图-放大功能')
    def test_homepage_ride_map_zoom_in(self, info):
        device = info.device
        try:
        # 回到首页并截图
            try:
                device(label="首页").click(timeout=1)
            except Exception as e:
                logger.info("可能已在首页")
            # 点击骑行按钮
            assert assert_element_exist(device(label="骑行"))
            device(label="骑行").click()
            # 点击放大按钮
            assert assert_element_exist(device.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other['
                                                     '1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Image[6]'))
            device.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other['
                         '1]/Other[1]/Other[2]/Other[2]/Other[2]/Other[2]/Other[2]/Image[6]').click()
            # 验证地图已放大
            assert assert_element_exist(device(label="用车规则"))
            attach_screenshot(device, '验证地图已放大后截图')
        except AssertionError as e:
            logger.error("验证骑行页面地图-放大功能失败")
            raise e
        except Exception as e:
            logger.error("验证骑行页面地图-放大功能失败，未知错误：{}".format(e))
            raise AssertionError("验证骑行页面地图-放大功能失败，未知错误：{}".format(e))
        finally:
            back_to_ride(device, info.bundle_id)
            back_to_homepage(device, info.bundle_id)