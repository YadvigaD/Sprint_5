from selenium.webdriver.common.by import By
import locators
import constants

class TestUserLogin:
    def test_user_login(self, driver):
        enter_button = driver.find_element(by=By.CSS_SELECTOR, value=locators.enter_button)
        enter_button.click()

        driver.implicitly_wait(2)

        email_input = driver.find_element(by=By.XPATH, value=locators.registration_email_input)
        email_input.send_keys(constants.exist_user_email)

        password_input = driver.find_element(by=By.XPATH, value=locators.registration_password_input)
        password_input.send_keys(constants.exist_user_passsword)

        login_button = driver.find_element(by=By.XPATH, value=locators.main_popup_button)
        login_button.click()

        driver.implicitly_wait(2)

        user_name = driver.find_element(by=By.XPATH, value=locators.user_name)
        user_avatar = driver.find_element(by=By.XPATH, value=locators.user_avatar)
        modal = driver.find_elements(By.XPATH, locators.modal)

        assert user_name.text == 'User.' and user_avatar.is_displayed and len(modal) == 0
