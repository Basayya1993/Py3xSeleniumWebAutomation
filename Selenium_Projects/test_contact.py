# Automation of Contact List of testing Website
# username : xitix24452@coloruz.com , pass: wingify@123
# https://thinking-tester-contact-list.herokuapp.com/contactList


import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from faker import Faker

faker = Faker()


@allure.title("Automated the Contact list website for the testing")
@allure.testcase("https://thinking-tester-contact-list.herokuapp.com/", name="ContactListApp")
@allure.tag("Contact List")
@allure.description("Verifying the contact list from the faker list")
@pytest.mark.contact_list
def test_contact_webpage():
    chrome_opt = webdriver.ChromeOptions()

    driver = webdriver.Chrome(chrome_opt)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")

    driver.maximize_window()
    time.sleep(5)

    email_contact = driver.find_element(By.XPATH, "//input[@id='email']")
    email_contact.send_keys("xitix24452@coloruz.com")

    password_contact = driver.find_element(By.XPATH, "//input[@id='password']")
    password_contact.send_keys("wingify@123")

    submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
    submit_btn.click()
    time.sleep(5)

    assert driver.current_url == "https://thinking-tester-contact-list.herokuapp.com/contactList"

    # //button[@id='add-contact']
    time.sleep(5)
    add_contact = driver.find_element(By.XPATH, "//button[@id='add-contact']")
    add_contact.click()
    time.sleep(3)

    info_first_name = driver.find_element(By.CSS_SELECTOR, "[id='firstName']")
    info_first_name.send_keys(faker.first_name())
    time.sleep(3)

    info_last_name = driver.find_element(By.CSS_SELECTOR, "[id='lastName']")
    info_last_name.send_keys(faker.last_name())
    time.sleep(3)

    # [id='birthdate']
    info_birthdate = driver.find_element(By.CSS_SELECTOR, "[id='birthdate']")
    birth_date = str(faker.date_of_birth(minimum_age=20, maximum_age=40))
    info_birthdate.send_keys(birth_date)
    time.sleep(3)

    # [id='email']
    info_email = driver.find_element(By.CSS_SELECTOR, "[id='email']")
    info_email.send_keys(faker.email())
    time.sleep(3)

    info_phone = driver.find_element(By.CSS_SELECTOR, "[id='phone']")
    info_phone.send_keys(faker.basic_phone_number())
    time.sleep(3)

    info_city = driver.find_element(By.CSS_SELECTOR, "[id='city']")
    info_city.send_keys(faker.city())
    time.sleep(3)

    info_state = driver.find_element(By.CSS_SELECTOR, "[id='stateProvince']")
    info_state.send_keys(faker.state())
    time.sleep(3)

    info_postal = driver.find_element(By.CSS_SELECTOR, "[id='postalCode']")
    info_postal.send_keys(faker.postcode())
    time.sleep(3)

    info_country = driver.find_element(By.CSS_SELECTOR, "[id='country']")
    info_country.send_keys(faker.country())
    time.sleep(3)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_btn.click()
    time.sleep(5)

    time.sleep(5)
    driver.quit()
