from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.create_order_locators import CreateOrderLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def sleep_while(self):
        element = EC.presence_of_element_located((By.XPATH, "//div[@class='Home_FAQ__3uVm4']"))
        WebDriverWait(self.driver, 10).until(element)

    def click_on_question(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].click();", element)

    def get_text_from_answer(self, a_locator):
        element = self.driver.find_element(*a_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(a_locator))
        return element.text

    def click_on_create_order_main_page(self):
        order = CreateOrderLocators()
        self.driver.find_element(*order.CREATE_ORDER_MAIN_PAGE_HEADER).click()

    def wait_redirect_url(self, expected_url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(expected_url))
