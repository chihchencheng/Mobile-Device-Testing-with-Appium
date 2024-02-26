import xml.dom.minidom
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')

APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '17.2',
    'deviceName': 'iPhone 15',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(APPIUM, CAPS)


try:
	time.sleep(4)
	wait = WebDriverWait(driver, 10)
	print(driver.page_source)
	# wait.until(EC.presence_of_element_located(
    #     (MobileBy.ACCESSIBILITY_ID, 'Login Screen')))
	# driver.find_element(MobileBy.CLASS_NAME, 'XCUIElementTypeStaticText')
	# driver.find_element(MobileBy.XPATH, '//XCUIElementTypeOther[@label="Webview Demo"]')
finally:
	driver.quit()