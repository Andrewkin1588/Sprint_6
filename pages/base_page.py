from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def button_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        return element.text

    def wait_redirect_url(self, expected_url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(expected_url))
