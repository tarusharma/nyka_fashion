import pytest

from locatorsofnykaa.nykaaloginpagelocators import *

from utilities.commonutilities import commonfunctions
from utilities.commonutilities import *
from utilities.loginpageutilities import *
from configofnykka.configdataofnykka import *


class TestLoginPage:
    @pytest.mark.usefixtures("initiate_driver")
    # @pytest.mark.parametrize('mobile_field', [("1233222222"), ("123456333333")])
    def test_verify_correct_login(self, initiate_driver):
        loginpage().performlogin(mobile_no)

        a= commonfunctions().get_element_text(assertion_login)
        print(a)
        assert a == "Download the Nykaa Fashion App & Get ₹150 off* | Use Code - NF150New", "incorrect otp no"

    @pytest.mark.parametrize('entr_mobile',
                             [("96522342356"), ("98765431"), (""), ("123456789")])
    def test_login_function_with_invalid_details(self, initiate_driver, entr_mobile):
        loginpage().performlogin(entr_mobile)
        b=commonfunctions().get_element_text(assert_invalid)
        print(b)
        assert b == "Please enter a valid mobile number!"


