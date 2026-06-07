from locators import Locators
from constants import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_click_login_button(self, driver):
        driver.get(BASE_URL)
        login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
        login_button.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))

    def test_click_personal_account(self, driver):
        driver.get(BASE_URL)
        personal_account = driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))

    def test_go_to_registration_page(self, driver):
        driver.get(LOGIN_URL)
        register_link = driver.find_element(*Locators.REGISTRATION_LINK)
        register_link.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(REGISTER_URL))

    def test_login_from_registration_form(self, driver):
        driver.get(REGISTER_URL)
        login_link = driver.find_element(*Locators.LOGIN_LINK_REGISTRATION_PAGE)
        login_link.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(LOGIN_URL))

    def test_go_to_forgot_password_page(self, driver):
        driver.get(LOGIN_URL)
        forgot_password_link = driver.find_element(*Locators.FORGOT_PASSWORD_LINK)
        forgot_password_link.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(FORGOT_PASSWORD_URL))

    def test_login(self, driver):
        driver.get(LOGIN_URL)
        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        email_input.send_keys("aida_test_2026@gmail.com")
        password_input.send_keys("123456")
        login_button.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.url_to_be(BASE_URL))