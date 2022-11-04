import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from configofnykka.configdataofnykka import *
from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")


@pytest.fixture()
def initiate_driver():
    driver.get(URL)
    driver.maximize_window()
    yield driver

    driver.quit()
