import time
from locators import Locators


def test_go_to_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    assert "/account" in driver.current_url


def test_go_to_constructor_from_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
    constructor_button.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/"


def test_logout(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    time.sleep(3)
    exit_button = driver.find_element(*Locators.LOGOUT_BUTTON)
    exit_button.click()
    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"


def test_go_to_constructor_by_logo(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    logo_button = driver.find_element(*Locators.LOGO_BUTTON)
    logo_button.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/"