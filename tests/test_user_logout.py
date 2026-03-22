from selenium.webdriver.common.by import By
import locators
import time

def test_user_logout(driver, exist_user):
    enter_button = driver.find_element(by=By.CSS_SELECTOR, value=locators.enter_button)
    enter_button.click()

    driver.implicitly_wait(2)

    email_input = driver.find_element(by=By.XPATH, value=locators.registration_email_input)
    email_input.send_keys(exist_user["email"])

    password_input = driver.find_element(by=By.XPATH, value=locators.registration_password_input)
    password_input.send_keys(exist_user["password"])

    login_button = driver.find_element(by=By.XPATH, value=locators.main_popup_button)
    login_button.click()

    driver.implicitly_wait(2)

    logout_button = driver.find_element(by=By.XPATH, value=locators.logout_button)
    logout_button.click()

    driver.implicitly_wait(2)

    enter_button = driver.find_element(by=By.CSS_SELECTOR, value=locators.enter_button)
    user_name = driver.find_elements(by=By.XPATH, value=locators.user_name)
    user_avatar = driver.find_elements(by=By.XPATH, value=locators.user_avatar)

    assert enter_button.text == 'Вход и регистрация' and len(user_avatar) == 0 and len(user_name) == 0
    driver.quit()
