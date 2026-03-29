import pytest
from selenium import webdriver
from faker import Faker
import constants

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get(constants.site_url)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def email():
    faker = Faker()
    return faker.email()
