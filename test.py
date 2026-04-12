from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
import time
import os 
from appium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.actions import interaction
from appium.webdriver.common.actions.pointer_input import PointerInput
 
options = XCUITestOptions()
options.platform_name = "iOS"
options.automation_name = "XCUITest"
# options.device_name = "iPhone"
# options.browser_name = "Safari"
# options.platform_version = os.getenv("IOS_VERSION", "18.5")
# options.platform_version = "17.0"

options.udid = os.environ.get("DEVICE_ID")
options.browser_name = "Safari"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

try:
    # 🌐 فتح موقع
    driver.get("https://viscend.vercel.app")
    time.sleep(10)

    # 📸 صورة أولى
    driver.save_screenshot("screen1.png")

    # 👆 محاولة النقر (أي مكان في الصفحة)
    driver.tap([(950, 520)])
    time.sleep(2)
    driver.tap([(520, 950)])
    time.sleep(2)

    # ⬇️ سحب / تمرير
    driver.execute_script("mobile: dragFromToForDuration", {
        "duration": 1.0,
        "fromX": 500,
        "fromY": 2000,
        "toX": 450,
        "toY": 900
    })

    driver.swipe(500, 2000, 450, 900, 1000)


     # def swipe(driver):
     #     finger = PointerInput(interaction.POINTER_TOUCH, "finger")
     #     actions = ActionChains(driver)
     #     actions.w3c_actions = interaction.ActionBuilder(driver, mouse=finger)
     
     #     actions.w3c_actions.pointer_action.move_to_location(500, 2000)
     #     actions.w3c_actions.pointer_action.pointer_down()
     #     actions.w3c_actions.pointer_action.pause(1.0)
     #     actions.w3c_actions.pointer_action.move_to_location(450, 900)
     #     actions.w3c_actions.pointer_action.pointer_up()
     
     #     actions.perform()

    time.sleep(2)
    driver.tap([(500, 1320)])
    time.sleep(2)
    driver.tap([(500, 1320)])
    time.sleep(3)

    # 📸 صورة ثانية
    driver.save_screenshot("screen2.png")

finally:
    driver.quit()
