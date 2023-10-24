import time

import allure

from common.log import logger
from common.custom_operation import assert_element_exist, force_tap
from common.attach_screenshot import attach_screenshot
from common.back_to_another_page import back_to_homepage, back_to_ride, restart_app


@allure.epic('[首页]模块')
@allure.feature('骑行页面-banner功能验证')
class TestHomepageRideBanner:
    @allure.title('验证骑行页面banner-找车功能')
    def test_homepage_ride_banner_find_bike(self, info):
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
        # 点击banner
        assert assert_element_exist(device(label="找车"))
        device(label="找车").click()
        # 等待地图加载
        time.sleep(3)
        # 验证地图已加载
        assert assert_element_exist(device(label="用车规则"))
        attach_screenshot(device, '点击banner-找车后截图')
        # 点击返回按钮
        back_to_ride(device, info.bundle_id)
    
    @allure.title('验证骑行页面banner-客服中心')
    def test_homepage_ride_banner_customer_service_center(self, info):
        device = info.device
        # 点击客服中心
        try:
            custom_service_center = device(label="客服中心").get(timeout=3)
            custom_service_center.click()
            # 通过【计费规则】验证是否进入客服中心
            assert assert_element_exist(device(label="计费规则"))
            attach_screenshot(device, '点击客服中心后截图')
            time.sleep(1)  # 等待页面加载
            # 点击返回按钮
            back_to_ride(device, info.bundle_id)
        except Exception as e:
            restart_app(device, info.bundle_id)
            device(label="骑行").click(timeout=3)
    
    @allure.title('验证骑行页面banner-故障上报')
    def test_homepage_ride_banner_fault_report(self, info):
        device = info.device
        # 验证上一步强制点击的时候 返回到首页了
        if assert_element_exist(device(label="骑行"), retry_times=3):
            device(label="骑行").click()
        # 点击故障上报
        assert assert_element_exist(device(label="故障上报"))
        device(label="故障上报").click()
        # 通过【上传车辆编号】文字验证是否进入故障上报页面
        assert assert_element_exist(device(label="上传车辆编号"))
        attach_screenshot(device, '点击故障上报后截图')
        # 点击返回按钮
        back_to_ride(device, info.bundle_id)
    
    @allure.title('验证骑行页面banner-申请停车点')
    def test_homepage_ride_banner_applying_parking_spot(self, info):
        device = info.device
        # 点击申请停车点
        assert assert_element_exist(device(label="申请停车点"))
        device(label="申请停车点").click()
        # 通过【用车】【停车】按钮文字验证是否进入申请停车点页面
        assert assert_element_exist(device(label="用车"))
        assert assert_element_exist(device(label="停车"))
        attach_screenshot(device, '点击申请停车点后截图')
        # 点击返回按钮
        back_to_ride(device, info.bundle_id)
    
    @allure.title('验证骑行页面banner-违规举报')
    def test_homepage_ride_banner_report_violation(self, info):
        device = info.device
        # 点击违规举报
        for i in range(5):
            # 滑动banner至违规举报
            device.swipe(0.8, 0.4, 0.2, 0.4)
            if assert_element_exist(device(label="违规举报"), retry_times=1):
                break
            time.sleep(1)
        device(label="违规举报").click()
        # 通过【上传违规车辆编号】文字验证是否进入违规举报页面
        assert assert_element_exist(device(label="上传违规车辆编号"))
        attach_screenshot(device, '点击违规举报后截图')
        # 点击返回按钮
        back_to_ride(device, info.bundle_id)
    
    @allure.title('验证骑行页面banner-今日福利')
    def test_homepage_ride_banner_today_welfare(self, info):
        device = info.device
        for i in range(5):
            # 滑动banner至今日福利
            device.swipe(0.8, 0.4, 0.2, 0.4)
            if assert_element_exist(device(label="今日福利"), retry_times=1):
                break
            time.sleep(1)
        device(label="今日福利").click()
        # 通过【优惠购卡专区】文字验证是否进入今日福利页面
        assert_element_exist(
            device.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/StaticText[1]'))
        assert device.xpath(
            '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/StaticText[1]').get().value == '优惠购卡专区', '进入今日福利页面失败'
        attach_screenshot(device, '点击今日福利后截图')
        # 点击返回按钮
        back_to_ride(device, info.bundle_id)
        back_to_homepage(device, info.bundle_id)
