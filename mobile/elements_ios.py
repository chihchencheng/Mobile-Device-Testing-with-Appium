from appium import webdriver
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
	wait = WebDriverWait(driver, 10)
	# TODO wait for the 'echo box' element and click to go to next screen
	wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
	# TODO wait for the input field and input 'Hello' in it
	wait.until((EC.presence_of_element_located(
		(MobileBy.ACCESSIBILITY_ID, 'messageInput')))).send_keys('Hello')
	# TODO click the save button
	driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
	saved_text = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
	assert saved_text == 'Hello'
	# TODO assert that the main screen
	driver.back()
	# TODO go back to the echo box view
	wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
	# TODO assert that the 'Hello' text is still displayed
	saved_text = wait.until(EC.presence_of_element_located(
		(MobileBy.ACCESSIBILITY_ID, 'savedMessage'))).text
	assert saved_text == 'Hello'
finally:
	driver.quit()