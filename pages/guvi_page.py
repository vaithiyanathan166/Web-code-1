from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GuviPage(BasePage):
    LOGIN_BUTTON = (By.LINK_TEXT, "login_button")
    SIGN_UP_BUTTON = (By.LINK_TEXT, "Sign up")
    EMAIL_INPUT = (By.ID, "login_email")
    PASSWORD_INPUT = (By.ID, "login-password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    LOGIN_BUTTON = (By.ID, "login_button")

    EMAIL_INPUT = (By.ID, "email")  # Update the locator to match your actual implementation
    PASSWORD_INPUT = (By.ID, "password")  # Update as needed
    SUBMIT_BUTTON = (By.ID, "submit-btn")  # Adjust the locator

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    # def click_login(self):
    #     self.click_element(self.login_button)

def click_login(self):
    self.click_element(self.LOGIN_BUTTON)

    



    def click_sign_up(self):
        self.click_element(self.SIGN_UP_BUTTON)

    # def login(self, email, password):
    #     self.click_login()
    #     self.click_login(self.login_button)
    #     self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
    #     self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
    #     self.click_element(self.SUBMIT_BUTTON)

    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
    
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')  # Adjust XPath based on actual HTML
    self.driver.save_screenshot("debug_login_button_visibility.png")
    print(self.driver.page_source)  # Logs the current HTML for debugging


####


