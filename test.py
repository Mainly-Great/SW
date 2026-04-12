from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
import time
import os 
 
options = XCUITestOptions()
options.platform_name = "iOS"
options.automation_name = "XCUITest"
# options.device_name = "iPhone"
# options.browser_name = "Safari"
# options.platform_version = os.getenv("IOS_VERSION", "18.5")
# options.platform_version = "17.0"

options.udid = os.environ.get("DEVICE_ID")

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

    driver.tap([(500, 1320)])
    driver.tap([(500, 1320)])
    time.sleep(3)

    # 📸 صورة ثانية
    driver.save_screenshot("screen2.png")

finally:
    driver.quit()
