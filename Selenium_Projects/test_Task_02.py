# Selenium Project#4 - Mini Project
# open the url - https://katalon-demo-cura.herokuapp.com/ click on the make appointment button
# verify that url changes - assert time.sleep(3) enter the username, password next page verify the current url
# make appointment text on the web page.Upload them Github.com

import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType


@allure.title("Selenium Mini Project - 4")
@allure.description("Verify the login-page and find the error message")
@allure.tag("Web-Automation using selenium for CURA Healthcare Service website")
@allure.severity("Medium")
@pytest.mark.Mini_Project
def test_cura_webpage():
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="webpage-screenshot", attachment_type=AttachmentType.PNG)

    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    message = driver.find_element(By.XPATH, "/html/body/header/div/h3")
    print(message.text)
    assert message.text == 'We Care About Your Health'
    allure.attach(driver.get_screenshot_as_png(), name="message-screenshot", attachment_type=AttachmentType.PNG)

    click_appointment = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    click_appointment.click()
    time.sleep(5)

    user_name = driver.find_element(By.XPATH, "//input[@name='username']")
    user_name.send_keys("admin")
    time.sleep(5)

    pass_word = driver.find_element(By.XPATH, "//input[@name='password']")
    pass_word.send_keys("123456")
    time.sleep(5)

    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()
    time.sleep(10)

    # //p[@class='lead text-danger']
    message_alert = driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
    print(message_alert.text)
    time.sleep(5)
    assert message_alert.text == 'Login failed! Please ensure the username and password are valid.'

    print(driver.current_url)
    assert driver.current_url == 'https://katalon-demo-cura.herokuapp.com/profile.php#login'

    allure.attach(driver.get_screenshot_as_png(), name="error_message-screenshot", attachment_type=AttachmentType.PNG)

    time.sleep(5)
    driver.quit()


