import pytest

from utilities.homepageutilitiesofnykaa import homepagefunction
from utilities.loginpageutilities import *
from configofnykka.configdataofnykka import *


class Test_homepage:
    @pytest.mark.usefixtures("initiate_driver")
    def test_verify_order1(self, initiate_driver):
        loginpage().performlogin(mobile_no)
        homepagefunction().perform_order(name_of_item)
        a = commonfunctions().get_element_text(buy_assert)
        print(a)
        assert a == "Add new address"
