from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sleep_while_not_located_faq_div(self):
        element = EC.presence_of_element_located((By.XPATH, "//div[@class='Home_FAQ__3uVm4']"))
        WebDriverWait(self.driver, 10).until(element)
