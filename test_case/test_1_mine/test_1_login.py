import pytest
import allure

from common.log import logger
from common.login import login
from common.custom_operation import swipe_by_direction,assert_element_exist
from common.attach_screenshot import attach_screenshot

@allure.epic('[我的]模块')
@allure.feature('登陆相关功能')
class TestMineLogin:
    @pytest.mark.order(1)
    @allure.title('验证已经登陆情况下对app退出登录')
    def test_mine_logout(self,info):
        device=info.device
        # 点击我的按钮
        device(label="我的").click()
        # 点击设置按钮
        device.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other['
                     '1]/CollectionView[1]/Cell[1]/Other[1]/Other[2]/Other[4]/Image[1]').click()
        attach_screenshot(device, '点击设置按钮后截图')
        # 滑动向上找到退出按钮
        swipe_by_direction(device, 'up')
        attach_screenshot(device, '滑动向上找到退出按钮后截图')
        # 点击退出按钮
        device.xpath('//Table/Button[1]/StaticText[1]').click()
        attach_screenshot(device, '点击退出按钮后截图')
        # 点击确认按钮
        device.xpath('//Alert/Other[1]/Other[1]/Other[2]/ScrollView[2]/Other[1]/Other[1]/Other[3]').click()
        attach_screenshot(device, '点击确认按钮后截图')
        assert assert_element_exist(device(label="点击登录/注册"))
        attach_screenshot(device, '退出登录后截图')
        logger.info("退出登录成功")
        
    @pytest.mark.order(2)
    @allure.title('验证未登录情况下对app登录')
    def test_mine_login(self,info):
        device=info.device
        assert login(device,user_name=info.user_name) is True
        logger.info("登录成功")
        attach_screenshot(device, '登录成功后截图')