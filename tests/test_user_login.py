from selenium.webdriver.common.by import By
import locators

def test_user_login(driver, exist_user):
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

    user_name = driver.find_element(by=By.XPATH, value=locators.user_name)
    user_avatar = driver.find_element(by=By.XPATH, value=locators.user_avatar)
    modal = driver.find_elements(By.XPATH, locators.modal)

    assert user_name.text == 'User.' and user_avatar.is_displayed and len(modal) == 0
    driver.quit()
