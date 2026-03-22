from selenium.webdriver.common.by import By
import locators

def test_inccorect_email_registration(driver, exist_user):
    enter_button = driver.find_element(by=By.CSS_SELECTOR, value=locators.enter_button)
    enter_button.click()

    driver.implicitly_wait(2)

    popup_no_account = driver.find_element(by=By.XPATH, value=locators.popup_no_account_button)
    popup_no_account.click()

    driver.implicitly_wait(2)

    email_input = driver.find_element(by=By.XPATH, value=locators.registration_email_input)
    email_input.send_keys(exist_user["email"])

    password_input = driver.find_element(by=By.XPATH, value=locators.registration_password_input)
    password_input.send_keys(exist_user["password"])

    password_confirm_input = driver.find_element(by=By.XPATH, value=locators.registration_password_confirm_input)
    password_confirm_input.send_keys(exist_user["password"])

    create_button = driver.find_element(by=By.XPATH, value=locators.main_popup_button)
    create_button.click()

    driver.implicitly_wait(2)

    form = driver.find_element(by=By.XPATH, value=locators.registration_form)
    driver.implicitly_wait(2)
    wrapped_error_inputs = len(form.find_elements(By.XPATH, locators.input_error_wrapper))
    driver.implicitly_wait(2)
    error_text = driver.find_element(by=By.XPATH, value=locators.span_error)

    assert error_text.text == 'Ошибка' and wrapped_error_inputs == 3
    driver.quit()
