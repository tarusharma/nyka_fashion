from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from configofnykka.configdataofnykka import *
from conftest import driver
#from locatorsofnykaa.homepagelocators import assert_order_summary
import time
class commonfunctions():

    def driver_wait(self,locator):
        if locator.startswith('//'):
            WebDriverWait(driver, explicit_wait_time).until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))
        else:
            WebDriverWait(driver, explicit_wait_time).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def get_element_text(self, element: str) -> str:
        self.driver_wait(element)
        text = driver.find_element(By.CSS_SELECTOR, element).text
        return text

    def click_element(self, locator):
        if locator.startswith('//'):
            WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,locator)))
            driver.find_element(By.XPATH, locator).click()
        else:
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            driver.find_element(By.CSS_SELECTOR, locator).click()

    def send_key(self,locator,itemname):
        if locator.startswith('//'):
            self.driver_wait(locator)
            driver.find_element(By.XPATH,locator).send_keys(itemname)
        else:
            self.driver_wait(locator)
            driver.find_element(By.CSS_SELECTOR, locator).send_keys(itemname)

