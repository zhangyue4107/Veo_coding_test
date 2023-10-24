import time


# 方向滑动
def swipe_by_direction(device, direction):
    if direction == 'up':
        device.swipe(0.5, 0.8, 0.5, 0.2)
        return True
    if direction == 'down':
        device.swipe(0.5, 0.2, 0.5, 0.8)
        return True
    if direction == 'left':
        device.swipe(0.8, 0.5, 0.2, 0.5)
        return True
    if direction == 'right':
        device.swipe(0.2, 0.5, 0.8, 0.5)
        return True
    else:
        return False


# 元素检测存在
def assert_element_exist(element, retry_times=5):
    for i in range(retry_times):
        if element.exists:
            return True
        else:
            time.sleep(1)
    return False


# 强制点击断言
def force_tap(device,x,y, element, retry_times=5):
    for i in range(retry_times):
        device.click(x,y)
        if assert_element_exist(element,retry_times=1):
            return True
    return False
    