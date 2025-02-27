from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.create_order_locators import CreateOrderLocators
from constants import YANDEX_URL


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_first_option_from_dropdown(self):
        element = self.driver.find_element(*CreateOrderLocators.INPUT_STATION)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def click_on_create_order_main_page(self):
        super().button_click(CreateOrderLocators.CREATE_ORDER_MAIN_PAGE_HEADER)

    def append_data_customer(self):
        super().send_keys(CreateOrderLocators.INPUT_NAME, 'Тест')
        super().send_keys(CreateOrderLocators.INPUT_LAST_NAME, 'Тестов')
        super().send_keys(CreateOrderLocators.INPUT_ADDRESS, 'Тестовая')
        super().send_keys(CreateOrderLocators.INPUT_PHONE_NUMBER, '89099999999')
        self.select_first_option_from_dropdown()

    def choice_data_in_calendar(self):
        super().button_click(CreateOrderLocators.INPUT_DATE_ORDER)
        super().button_click(CreateOrderLocators.CALENDAR_DATA)

    def choice_rent_term(self):
        super().button_click(CreateOrderLocators.DROPDOWN_RENT_TERM)
        super().button_click(CreateOrderLocators.SELECT_RENT_TERM)

    def click_on_button_next(self):
        super().button_click(CreateOrderLocators.BUTTON_NEXT)

    def click_button_yes_on_modal_window(self):
        super().button_click(CreateOrderLocators.BUTTON_YES_POPUP)

    def get_text_complete_order_from_modal_window(self):
        return super().get_text(CreateOrderLocators.TEXT_COMPLETED_ORDER)

    def click_check_order_status(self):
        super().button_click(CreateOrderLocators.BUTTON_CHECK_STATUS)

    def click_logo_scooter(self):
        super().button_click(CreateOrderLocators.LINK_SCOOTER_LOGO)

    def click_logo_yandex(self):
        super().button_click(CreateOrderLocators.LINK_YANDEX_LOGO)
        super().wait_redirect_url(YANDEX_URL)

