import time

from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locatorsofnykaa.nykaahomepagelocators import *
from conftest import driver
from locatorsofnykaa.nykaaloginpagelocators import *
from utilities.commonutilities import *
from configofnykka.configdataofnykka import *
from selenium.webdriver.support.select import Select

class loginpage():

    def click_on_account_btn(self):
        commonfunctions().click_element(account_btn)

    def login_signup_btn(self):
       commonfunctions().click_element(login_signup_btn)

    def enter_the_mobile(self,itemname):
        commonfunctions().send_key(entr_mobile,itemname)

    def click_on_submit(self):
        commonfunctions().click_element(submit_btn)

    def click_on_verify(self):
        commonfunctions().click_element(verify_otp)
        time.sleep(20)

    def performlogin(self,itemname):
        self.click_on_account_btn()
        self.login_signup_btn()
        self.enter_the_mobile(itemname)
        self.click_on_submit()
        self.click_on_verify()






