from selenium import webdriver
from selenium.webdriver.common import by
import time


def test_chrome():
    driver = webdriver.Chrome()
    driver.get("https://google.co.in")
    driver.maximize_window()
    time.sleep(5)

    driver.quit()
