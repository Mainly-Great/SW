from appium import webdriver
from appium.options.ios import XCUITestOptions
import time
import os

options = XCUITestOptions()
options.platform_name = "iOS"
options.automation_name = "XCUITest"
options.udid = os.environ.get("DEVICE_ID")
options.browser_name = "Safari"

options.set_capability("useNewWDA", True)
options.set_capability("wdaLocalPort", 8100)
options.set_capability("wdaLaunchTimeout", 120000)
options.set_capability("wdaConnectionTimeout", 120000)
options.set_capability("showXcodeLog", True)
options.set_capability("wdaStartupRetries", 2)
options.set_capability("wdaStartupRetryInterval", 20000)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # فتح الموقع
    driver.get("https://cryptu-compass.netlify.app/")
    time.sleep(8) 

    # 📸 صورة 1
    driver.save_screenshot("screen1.png")

    # 👆 نقر بالإحداثيات (الطريقة الصحيحة)
    driver.execute_script("mobile: tap", {
        "x": 950,
        "y": 520
    })
    time.sleep(2)

    driver.execute_script("mobile: tap", {
        "x": 520,
        "y": 950
    })
    time.sleep(2)

    # ⬇️ تمرير (بديل drag)
    driver.execute_script("mobile: swipe", {
        "direction": "up"
    })

    time.sleep(3)

    driver.execute_script("mobile: tap", {
        "x": 500,
        "y": 1320
    })

    time.sleep(3)

    # 📸 صورة 2
    driver.save_screenshot("screen2.png")

finally:
    driver.quit()
# ------------------------------------------------------------------------

# from appium import webdriver
# from appium.options.ios import XCUITestOptions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# import time, os

# options = XCUITestOptions()
# options.platform_name = "iOS"
# options.automation_name = "XCUITest"
# options.udid = os.environ.get("DEVICE_ID")
# options.browser_name = "Safari"

# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# def tap(driver, x, y):
#     finger = PointerInput(interaction.POINTER_TOUCH, "finger")
#     actions = ActionChains(driver)
#     actions.w3c_actions = interaction.ActionBuilder(driver, mouse=finger)

#     actions.w3c_actions.pointer_action.move_to_location(x, y)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.pause(0.1)
#     actions.w3c_actions.pointer_action.pointer_up()
#     actions.perform()

# def swipe(driver, x1, y1, x2, y2):
#     finger = PointerInput(interaction.POINTER_TOUCH, "finger")
#     actions = ActionChains(driver)
#     actions.w3c_actions = interaction.ActionBuilder(driver, mouse=finger)

#     actions.w3c_actions.pointer_action.move_to_location(x1, y1)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.pause(1.0)
#     actions.w3c_actions.pointer_action.move_to_location(x2, y2)
#     actions.w3c_actions.pointer_action.pointer_up()
#     actions.perform()

# try:
#     driver.get("https://viscend.vercel.app")
#     time.sleep(10)

#     driver.save_screenshot("screen1.png")

#     # 👆 نقرات (نفس إحداثياتك)
#     tap(driver, 950, 520)
#     time.sleep(2)

#     tap(driver, 520, 950)
#     time.sleep(2)

#     # ⬇️ تمرير (مرة واحدة فقط)
#     swipe(driver, 500, 2000, 450, 900)
#     time.sleep(2)

#     tap(driver, 500, 1320)
#     time.sleep(2)

#     tap(driver, 500, 1320)
#     time.sleep(3)

#     driver.save_screenshot("screen2.png")

# finally:
#     driver.quit()

# -----------------------------------------------------------------------
# from appium import webdriver
# from appium.options.ios import XCUITestOptions
# from selenium.webdriver.common.by import By
# import time
# import os 
# # from appium.webdriver.common.action_chains import ActionChains
# # from appium.webdriver.common.actions import interaction
# # from appium.webdriver.common.actions.pointer_input import PointerInput
 
# options = XCUITestOptions()
# options.platform_name = "iOS"
# options.automation_name = "XCUITest"
# # options.device_name = "iPhone"
# # options.browser_name = "Safari"
# # options.platform_version = os.getenv("IOS_VERSION", "18.5")
# # options.platform_version = "17.0"

# options.udid = os.environ.get("DEVICE_ID")
# options.browser_name = "Safari"

# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# # driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

# try:
#     # 🌐 فتح موقع
#     driver.get("https://viscend.vercel.app")
#     time.sleep(10)

#     # 📸 صورة أولى
#     driver.save_screenshot("screen1.png")

#     # 👆 محاولة النقر (أي مكان في الصفحة)
#     driver.tap([(950, 520)])
#     time.sleep(2)
#     driver.tap([(520, 950)])
#     time.sleep(2)

#     # ⬇️ سحب / تمرير
#     driver.execute_script("mobile: dragFromToForDuration", {
#         "duration": 1.0,
#         "fromX": 500,
#         "fromY": 2000,
#         "toX": 450,
#         "toY": 900
#     })

#     driver.swipe(500, 2000, 450, 900, 1000)


#      # def swipe(driver):
#      #     finger = PointerInput(interaction.POINTER_TOUCH, "finger")
#      #     actions = ActionChains(driver)
#      #     actions.w3c_actions = interaction.ActionBuilder(driver, mouse=finger)
     
#      #     actions.w3c_actions.pointer_action.move_to_location(500, 2000)
#      #     actions.w3c_actions.pointer_action.pointer_down()
#      #     actions.w3c_actions.pointer_action.pause(1.0)
#      #     actions.w3c_actions.pointer_action.move_to_location(450, 900)
#      #     actions.w3c_actions.pointer_action.pointer_up()
     
#      #     actions.perform()

#     time.sleep(2)
#     driver.tap([(500, 1320)])
#     time.sleep(2)
#     driver.tap([(500, 1320)])
#     time.sleep(3)

#     # 📸 صورة ثانية
#     driver.save_screenshot("screen2.png")

# finally:
#     driver.quit()
