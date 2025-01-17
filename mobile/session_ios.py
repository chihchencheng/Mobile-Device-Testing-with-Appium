from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')

APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '17.0',
    'deviceName': 'iPhone 15 Pro',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
driver.quit()