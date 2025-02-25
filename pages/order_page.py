from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.create_order_locators import CreateOrderLocators
from selenium.webdriver.common.keys import Keys


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def button_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def select_option(self):
        element = self.driver.find_element(*CreateOrderLocators.INPUT_STATION)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
