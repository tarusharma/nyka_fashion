import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from configofnykka.configdataofnykka import *
driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def initiate_driver():
    driver.get(URL)
    driver.maximize_window()
    yield driver

    driver.quit()
