import pytest

from locatorsofnykaa.nykaaloginpagelocators import *

from utilities.commonutilities import commonfunctions
from utilities.commonutilities import *
from utilities.loginpageutilities import *
from configofnykka.configdataofnykka import *

class homepagefunction():
    def searching_of_product(self, itemname):

        m = driver.find_element(By.XPATH, search_bar)
        m.send_keys(itemname)
        m.send_keys(Keys.ENTER)

    def click_on_item(self):

        commonfunctions().click_element(click_item)
        time.sleep(2)

    def select_size(self):
        commonfunctions().click_element(add_size)


    def add_to_cart(self):
        commonfunctions().click_element(add_to_bag)
        #driver.find_element(By.CSS_SELECTOR,add_to_bag)

    def view_to_bag(self):
        driver.find_element(By.XPATH,view_bag).click()
         #commonfunctions().click_element(add_to_bag)
        #time.sleep(8)
    def proceed_to_buy(self):
      driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Nykaa Fashion Cart']"))
      driver.find_element(By.XPATH,buy_iframe).click()
      time.sleep(3)

    def switch_tab(self):
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        #time.sleep(9)

    def perform_order(self,itemname):
        self.searching_of_product(itemname)
        self.click_on_item()
        self.switch_tab()
        self.select_size()
        self.add_to_cart()
        time.sleep(3)
        self.view_to_bag()
        time.sleep(9)
        self.proceed_to_buy()















