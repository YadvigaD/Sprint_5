from selenium.webdriver.common.by import By
import locators
import constants

class TestPlaceAuthAd:
    def test_place_auth_ad(self, driver):
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

        place_button = driver.find_element(by=By.XPATH, value=locators.place_ad)
        place_button.click()
        driver.implicitly_wait(2)


        name = "Продам гараж"
        name_input = driver.find_element(by=By.XPATH, value=locators.place_ad_title_input)
        name_input.send_keys(name)
        desc_input = driver.find_element(by=By.XPATH, value=locators.place_ad_description_input)
        desc_input.send_keys('Хороший гараж, недорого')
        price_input = driver.find_element(by=By.XPATH, value=locators.place_ad_price_input)
        price_input.send_keys('1000000') 

        category_choose_variant = driver.find_element(by=By.XPATH, value=locators.place_ad_category_open_button)
        category_choose_variant.click()
        driver.find_element(by=By.XPATH, value=locators.place_ad_category_car_variant).click()

        driver.implicitly_wait(2)

        city_choose_variant = driver.find_element(by=By.XPATH, value=locators.place_ad_city_open_button)
        city_choose_variant.click()
        driver.find_element(by=By.XPATH, value=locators.place_ad_city_variant).click()
        
        driver.implicitly_wait(2)

        driver.find_element(by=By.XPATH, value=locators.place_ad_radio).click()

        driver.find_element(by=By.XPATH, value=locators.place_ad_submit_button).click()

        driver.implicitly_wait(2)

        driver.find_element(by=By.XPATH, value=locators.my_profile).click()

        driver.implicitly_wait(2)

        ad = driver.find_element(by=By.XPATH, value=locators.in_profile_ad)

        assert ad.text == name
