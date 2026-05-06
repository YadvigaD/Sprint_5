from selenium.webdriver.common.by import By
import locators

class TestRegistarion:
    def test_registration(self, driver, email):
        enter_button = driver.find_element(by=By.CSS_SELECTOR, value=locators.enter_button)
        enter_button.click()

        driver.implicitly_wait(2)

        popup_no_account = driver.find_element(by=By.XPATH, value=locators.popup_no_account_button)
        popup_no_account.click()

        driver.implicitly_wait(2)

        form = driver.find_element(by=By.XPATH, value=locators.registration_form)

        email_input = form.find_element(by=By.XPATH, value=locators.registration_email_input)
        email_input.send_keys(email)

        password = "1234qwerty"

        password_input = form.find_element(by=By.XPATH, value=locators.registration_password_input)
        password_input.send_keys(password)

        password_confirm_input = form.find_element(by=By.XPATH, value=locators.registration_password_confirm_input)
        password_confirm_input.send_keys(password)

        create_button = driver.find_element(by=By.XPATH, value=locators.main_popup_button)
        create_button.click()

        driver.implicitly_wait(2)

        user_name = driver.find_element(by=By.XPATH, value=locators.user_name)
        user_avatar = driver.find_element(by=By.XPATH, value=locators.user_avatar)
        modal = driver.find_elements(By.XPATH, locators.modal)

        assert user_name.text == 'User.' and user_avatar.is_displayed and len(modal) == 0
