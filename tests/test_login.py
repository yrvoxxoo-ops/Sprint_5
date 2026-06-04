from locators import Locators
import time

def test_click_login_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    login_button.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"


def test_click_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"


def test_go_to_registration_page(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    register_link = driver.find_element(*Locators.REGISTRATION_LINK)
    register_link.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/register"


def test_login_from_registration_form(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    login_link = driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_PAGE)
    login_link.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"


def test_go_to_forgot_password_page(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    forgot_password_link = driver.find_element(*Locators.FORGOT_PASSWORD_LINK)
    forgot_password_link.click()
    assert driver.current_url == "https://stellarburgers.education-services.ru/forgot-password"


def test_login(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.education-services.ru/"