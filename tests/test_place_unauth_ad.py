from selenium.webdriver.common.by import By
import locators

class TestPlaceUnauthAd:
    def test_place_unauth_ad(self, driver):
        place_button = driver.find_element(by=By.XPATH, value=locators.place_ad)
        place_button.click()

        driver.implicitly_wait(2)

        title = driver.find_element(by=By.XPATH, value=locators.unauth_place_ad_title)

        assert title.text == 'Чтобы разместить объявление, авторизуйтесь'
