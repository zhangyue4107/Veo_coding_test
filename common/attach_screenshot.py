import time, allure


def attach_screenshot(device, name):
    screenshot_name = "{}-{}.png".format(name, time.strftime('%Y-%m-%d-%H-%M-%S'))
    device.screenshot('./screenshots/{}'.format(screenshot_name))
    allure.attach.file('./screenshots/{}'.format(screenshot_name), name, allure.attachment_type.PNG)
