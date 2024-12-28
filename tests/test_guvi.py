import pytest
from selenium import webdriver
from pages.guvi_page import GuviPage

URL = "https://www.guvi.in/"
VALID_EMAIL = "your_valid_email@example.com"
VALID_PASSWORD = "your_valid_password"
INVALID_EMAIL = "invalid_email@example.com"
INVALID_PASSWORD = "invalid_password"



def test_url_is_valid(driver):
    page = GuviPage(driver)
    page.open_url(URL)
    assert "GUVI" in page.get_title()

def test_page_title(driver):
    page = GuviPage(driver)
    page.open_url(URL)
    assert page.get_title() == "GUVI | Learn to code in your native language"

# def test_login_button_visibility(driver):
#      page = GuviPage(driver)
#      page.open_url(URL)
#      assert page.is_element_visible(GuviPage.LOGIN_BUTTON)

def test_login_button_visibility(driver):
     page = GuviPage(driver)
     page.open_url(URL)
     assert page.is_element_visible(GuviPage.LOGIN_BUTTON), "Login button is not visible"

def test_sign_up_button_visibility(driver):
     page = GuviPage(driver)
     page.open_url(URL)
     assert page.is_element_visible(GuviPage.SIGN_UP_BUTTON)

def test_sign_up_button_click(driver):
    page = GuviPage(driver)
    page.open_url(URL)
    page.click_register()
   





# def test_sign_up_button_click(driver):
#     page = GuviPage(driver)
#     page.open_url(URL)
#     page.click_sign_up()
#     assert "sign-in" in driver.current_url

# def test_sign_up_button_click(driver):
#      page = GuviPage(driver)
#      page.open_url(URL)
#      page.click_sign_up()
#      assert "register" in driver.current_url

def test_sign_up_button_click(driver):
    page = GuviPage(driver)
    page.open_url(URL)
    page.click_SIGN_uP()
    assert "register" in driver.current_url

def test_valid_login_and_logout(driver):
     page = GuviPage(driver)
     page.open_url(URL)
     page.login(VALID_EMAIL, VALID_PASSWORD)
     assert "dashboard" in driver.current_url  # Update as per actual dashboard URL or identifier
     page.logout()
     assert page.is_element_visible(GuviPage.login_button)
   

def test_invalid_login(driver):
    page = GuviPage(driver)
    page.open_url(URL)
    page.login(INVALID_EMAIL, INVALID_PASSWORD)
    # assert page.is_element_visible(GuviPage.Invalid email or password ) )in page.get_error_message()
    assert "Invalid email or password" in page.get_error_message(), "Error message not displayed or incorrect."


