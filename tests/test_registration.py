from helpers import generate_email
from locators import Locators
from constants import REGISTER_URL, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(REGISTER_URL)
        email = generate_email()
        name_input = driver.find_element(*Locators.NAME_INPUT)
        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        register_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        name_input.send_keys("Аида")
        email_input.send_keys(email)
        password_input.send_keys("123456")
        register_button.click()
        assert WebDriverWait(driver, 5).until(EC.url_to_be(LOGIN_URL))

    def test_registration_with_invalid_password(self, driver):
        driver.get(REGISTER_URL)
        email = generate_email()
        name_input = driver.find_element(*Locators.NAME_INPUT)
        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        register_button = driver.find_element(*Locators.REGISTRATION_BUTTON)
        name_input.send_keys("Аида")
        email_input.send_keys(email)
        password_input.send_keys("12345")
        register_button.click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_ERROR))