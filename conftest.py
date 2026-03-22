import pytest
from selenium import webdriver
from faker import Faker

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.implicitly_wait(5)
    return driver

@pytest.fixture(autouse=True)
def email():
    faker = Faker()
    return faker.email()

@pytest.fixture(autouse=True)
def exist_user():
    return {
        "email": "sprint5@practikum.ru",
        "password": "sprint5@practikum.ru"
    }