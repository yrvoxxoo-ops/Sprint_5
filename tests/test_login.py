from locators import Locators
from constants import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_click_login_button(driver):
    driver.get(BASE_URL)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    login_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL


def test_click_personal_account(driver):
    driver.get(BASE_URL)
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL


def test_go_to_registration_page(driver):
    driver.get(LOGIN_URL)
    register_link = driver.find_element(*Locators.REGISTRATION_LINK)
    register_link.click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(REGISTER_URL))
    assert driver.current_url == REGISTER_URL


def test_login_from_registration_form(driver):
    driver.get(REGISTER_URL)
    login_link = driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_PAGE)
    login_link.click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL


def test_go_to_forgot_password_page(driver):
    driver.get(LOGIN_URL)
    forgot_password_link = driver.find_element(*Locators.FORGOT_PASSWORD_LINK)
    forgot_password_link.click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(FORGOT_PASSWORD_URL))
    assert driver.current_url == FORGOT_PASSWORD_URL


def test_login(driver):
    driver.get(LOGIN_URL)
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL