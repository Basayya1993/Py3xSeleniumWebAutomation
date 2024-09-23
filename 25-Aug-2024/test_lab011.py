import time

from selenium import webdriver
from selenium.webdriver.common.by import By



def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://google.co.in")

    print(driver.title)
    time.sleep(5)
    driver.quit()


