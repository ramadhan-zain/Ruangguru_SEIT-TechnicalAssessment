from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    search_bar = (By.XPATH, "//input[@type='text']")
    search_icon = (By.XPATH, "//div[@class='css-13ksas7']")
    search_result_sum = (By.XPATH, "//span[@data-testid='total-result']")
    search_result_query = (By.XPATH, "//span[@data-testid='current-keyword']")

    def get_search_bar(self):
        return self.driver.find_element(*HomePage.search_bar)

    def get_search_icon(self):
        return self.driver.find_element(*HomePage.search_icon)

    def get_search_result_sum(self):
        return self.wait.until(EC.presence_of_element_located((HomePage.search_result_sum)))

    def get_search_result_query(self):
        return self.wait.until(EC.presence_of_element_located((HomePage.search_result_query)))

