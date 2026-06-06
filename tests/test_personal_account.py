from locators import Locators
from constants import BASE_URL, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_personal_account(driver):
    driver.get(LOGIN_URL)
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    WebDriverWait(driver, 5).until(EC.url_contains("/account"))
    assert "/account" in driver.current_url


def test_go_to_constructor_from_personal_account(driver):
    driver.get(LOGIN_URL)
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
    WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL


def test_logout(driver):
    driver.get(LOGIN_URL)
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    login_button = driver.find_element(*Locators.LOGIN_BUTTON)
    email_input.send_keys("aida_test_2026@gmail.com")
    password_input.send_keys("123456")
    login_button.click()
    personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
    personal_account.click()
    exit_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
    exit_button.click()
    WebDriverWait(driver, 5).until(EC.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL


def test_go_to_constructor_by_logo(driver):
    driver.get(LOGIN_URL)
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
    WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL