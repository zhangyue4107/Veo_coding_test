# 测试策略
## 测试目标：
- 确保哈啰单车App的功能和性能符合用户需求和期望。
- 验证App的可用性、稳定性、安全性和易用性。
- 发现并纠正任何潜在的缺陷、错误或漏洞。
## 测试类型：
- 功能测试：验证每个功能是否符合规格说明书、是否满足用户需求和期望。
- 兼容性测试：验证应用程序在各种不同的设备、操作系统和网络环境下的兼容性。
- 性能测试：验证应用程序在不同的负载和压力下的性能表现。
- 安全测试：验证应用程序的安全性和隐私保护机制是否符合相关法规和标准。
- 用户体验测试：验证应用程序的界面设计、交互方式和易用性是否符合用户习惯和期望。
## 测试环境：
- 操作系统：iOS 和 Android。
- 设备：iPhone 和 Android 手机。
- 网络环境：Wi-Fi 和移动数据网络。
- 测试工具：Facebook_wda、Wireshark 等。
## 测试范围：
1. 功能测试
   - 用户注册和登录功能测试。
   - 单车预订和还车功能测试。
   - 单车定位和导航功能测试。
   - 付款和退款功能测试。
   - 用户反馈和客户服务功能测试。
2. 兼容性测试
   - IOS软件版本: ios14.x ios15.x ios16.x
   - Android软件版本：Android9 Android10 Android11
3. 性能测试
   - IOS渲染性能测试
   - Android渲染性能测试
   - 服务端压力测试
4. 安全测试，
   - 数据加密验证
   - 用户身份验证
   - 隐私保护验证
5. 用户体验测试
   - 界面设计验证
   - 交互方式验证
   - 易用性验证
   - 可靠性验证
   - 反馈与响应速度验证

# 构思以及实施步骤
## 测试方案
### 测试用例准备
本次测试前，通过对哈喽单车的观察，识别哈啰app的主要功能，确定核心测试点，同时根据核心功能点编写测试用例，由于时间关系，部分测试用例未完成 
### 测试框架设计
本次测试采用Facebook_wda作为ios的控制端，同时使用allure对测试时间已经测试用例执行过程进行监控，并最终生成测试报告。
  - common.
    - attach_screenshot 对测试过程中关键断言进行截图
    - back_to_another_page 在每一测试用例执行之后，通过finally执行返回某一页面，方便后续用例执行
    - custom_operation 对于强制点击，拖拽等一些动作进行封装，避免重复点击和误点击
    - environment 对与测试环境进行区分
    - log 测试log配置文件
    - login 对于单独模块执行时，预先进行登录操作，
  - logs：测试过程中产生的log
  - screenshots 测试过程中截图 每次重新执行时会清除上次测试的截图
  - test_case
    - test_1_mine app-我的 模块测试用例
      - test_1_login 【我的】模块下，登陆相关测试用例
    - test_2_homepage app-首页 模块相关用例
      - test_1_ride 【首页】模块下， 骑行功能的相关用例
        - test_1_scan_code 骑行页面下 扫描二维码用例
        - test_2_map 骑行页面下  地图放大功能相关用例
        - test_3_banner 骑行页面下  banner相关功能测试用例
  - allure-report allure生成测试报告的元数据 使用 allure server ./allure-report 可生成测试报告
  - conftest.py pytest全局fixture注册与使用，包括环境变量注入，以及测试前检测app打开，测试后app关闭
  - run.py  程序运行文件  使用python3 run.py --env=dev
### 测试方案的优势与不足
#### 优势
   - 对测试执行时环境参数做了预留，方便后面对测试环境进行区分
   - 对不同模块的测试进行了执行完成后统一回到首页，方便后续按照模块执行测试用例
#### 不足
   - 执行效率较低，10条用例执行总耗时在100s左右，后续通过智能等待或异步等待进行调优
   - 没有引入OpenCV的图片对比机制，断言可能不准确，时间原因后续处理
   - cicd未引入，原本写好了dockerfile但是后续可能改动较大放弃上传
   - 因条件限制与时间原因，首次下载后的权限通知与弹窗未处理，后续有ipa包以及时间可以通过注册回调函数解决，但是这次实在是没时间了
   - 第一次做ios的自动化测试 可能从学习到实施的时间较短，还有大量隐藏问题未发现


## 实施步骤
1. 首先下载https://github.com/appium/WebDriverAgent 之后通过xcode改变bundle_id 安装测试客户端至iphone13
2. 安装 tidevice 通过命令tidevice -u 00008110-xxxxxxxxxxxx wdaproxy -B com.facebook.WebDriverAgentRunnerZhangy.xctrunner --port 8200 命令将wda转发到8200端口
3. 在iPhone上对wda的证书以及xctest的使用进行授权
4. 通过 python3 -m weditor 进行投屏并对元素进行定位
5. 框架内通过facebook_wda 绑定 localhost:8200进行通信
6. 启动 bundle_id=com.jingyao.EasyBike 的app 配合前面的weditor定位实现对ios端的控制
7. 控制并对预先的测试用例进行实现
8. 使用allure 以及pytest对测试结收集并统计代码覆盖率等相关信息

