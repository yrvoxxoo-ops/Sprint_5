import time
from helpers import generate_email
from locators import Locators


def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    email = generate_email()
    name_input = driver.find_element(*Locators.NAME_INPUT)
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    register_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
    name_input.send_keys("Аида")
    email_input.send_keys(email)
    password_input.send_keys("123456")
    register_button.click()
    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"


def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    email = generate_email()
    name_input = driver.find_element(*Locators.NAME_INPUT)
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    register_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
    name_input.send_keys("Аида")
    email_input.send_keys(email)
    password_input.send_keys("12345")
    register_button.click()
    error_text = driver.find_element(*Locators.INVALID_PASSWORD_ERROR)
    assert error_text.is_displayed()