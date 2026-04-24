from appium import webdriver
from appium.options.ios import XCUITestOptions
import time
import os
import random

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
    driver.get("https://cryptu-compass.netlify.app")
    time.sleep(8) 


    # اختبار توليد قيم عشوائية
    x = random.randint(100, 1000)
    y = random.randint(250, 2222)
    
    # استخدام القيم في الأمر
    driver.execute_script("mobile: tap", {
        "x": x,
        "y": y
    })
    # 👆 نقر بالإحداثيات (الطريقة الصحيحة)
    driver.execute_script("mobile: tap", {
        "x": 950,
        "y": 520
    })
    time.sleep(2)
    x = random.randint(100, 1000)
    y = random.randint(250, 2222)
    
    # استخدام القيم في الأمر
    driver.execute_script("mobile: tap", {
        "x": x,
        "y": y
    })
    x = random.randint(100, 1000)
    y = random.randint(250, 2222)
    
    # استخدام القيم في الأمر
    driver.execute_script("mobile: tap", {
        "x": x,
        "y": y
    })
    
    driver.execute_script("mobile: tap", {
        "x": 950,
        "y": 520
    })
    time.sleep(2)
    driver.execute_script("mobile: tap", {
        "x": 500,
        "y": 1850
    })
    time.sleep(2)
    
    x = random.randint(100, 1000)
    y = random.randint(250, 2222)
    # استخدام القيم في الأمر
    driver.execute_script("mobile: tap", {
        "x": x,
        "y": y
    })
    
    driver.execute_script("mobile: tap", {
        "x": 375,
        "y": 2220
    })
    time.sleep(2)
    driver.execute_script("mobile: tap", {
        "x": 785,
        "y": 2144
    })

    driver.execute_script("mobile: tap", {
        "x": 520,
        "y": 950
    })
    time.sleep(2)
    
    driver.execute_script("mobile: tap", {
        "x": 580,
        "y": 1620
    })
    driver.execute_script("mobile: swipe", {
        "direction": "up"
    })
    time.sleep(2)
    driver.execute_script("mobile: tap", {
        "x": 620,
        "y": 1820
    })
    

    # ⬇️ تمرير (بديل drag)
    driver.execute_script("mobile: swipe", {
        "direction": "up"
    })
    time.sleep(2)

    driver.execute_script("mobile: dragFromToForDuration", {
        "duration": 1.0,
        "fromX": 500,
        "fromY": 2000,
        "toX": 450,
        "toY": 900
    })
    time.sleep(3)

    driver.execute_script("mobile: tap", {
        "x": 930,
        "y": 1320
    })

    time.sleep(3)
    x = random.randint(100, 1000)
    y = random.randint(250, 2222)
    # استخدام القيم في الأمر
    driver.execute_script("mobile: tap", {
        "x": x,
        "y": y
    })


finally:
    driver.quit()
