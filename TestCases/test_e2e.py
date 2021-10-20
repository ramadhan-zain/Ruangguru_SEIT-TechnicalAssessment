import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.SearchData import SearchData


class TestFunctional(BaseClass):

    def test_e2e(self, setup, get_data):
        driver = self.driver
        wait = self.wait
        home_page = HomePage(driver, wait)

        # text_search = "test automation"

        home_page.get_search_bar().send_keys(get_data["query"])
        home_page.get_search_icon().click()

        # text = home_page.get_min_result().text
        # print(text)
        # home_page.get_min_result()

        jumlah_hasil = home_page.get_search_result_sum().text
        print(f"\nnumber of search results: {jumlah_hasil}")

        search_result = home_page.get_search_result_query().text
        print(f"search results: {search_result}")

        assert get_data["query"] in search_result

        # driver.refresh()
        home_page.get_search_bar().clear()

    @pytest.fixture(params=SearchData.test_HomePage_data)
    def get_data(self, request):
        return request.param