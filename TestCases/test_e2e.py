import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup):
        driver = self.driver
        wait = self.wait
        home_page = HomePage(driver, wait)

        home_page.get_search_bar().send_keys("test automation")
        home_page.get_search_icon().click()

        # text = home_page.get_min_result().text
        # print(text)
        # home_page.get_min_result()

        jumlah_hasil = home_page.get_search_result_sum().text
        print(jumlah_hasil)
