from locators import Locators
from constants import BASE_URL

def test_go_to_sauces_section(driver):
    driver.get(BASE_URL)
    sauces_tab = driver.find_element(*Locators.SAUCES_TAB)
    sauces_tab.click()
    assert "tab_tab_type_current" in sauces_tab.get_attribute("class")


def test_go_to_fillings_section(driver):
    driver.get(BASE_URL)
    fillings_tab = driver.find_element(*Locators.FILLINGS_TAB)
    fillings_tab.click()
    assert "tab_tab_type_current" in fillings_tab.get_attribute("class")


def test_go_to_buns_section(driver):
    driver.get(BASE_URL)
    sauces_tab = driver.find_element(*Locators.SAUCES_TAB)
    sauces_tab.click()
    buns_tab = driver.find_element(*Locators.BUNS_TAB)
    buns_tab.click()
    assert "tab_tab_type_current" in buns_tab.get_attribute("class")