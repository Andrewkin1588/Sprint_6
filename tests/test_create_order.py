import allure
from constants import *
from pages.order_page import OrderPage


class TestCreateOrder:
    def test_create_order(self, browser):
        with allure.step("Переходим на главную страницу"):
            browser.get(URL)
            o_page = OrderPage(browser)
        with allure.step("Нажимаем на кнопку 'Заказать'"):
            o_page.click_on_create_order_main_page()
        with allure.step("Заполняем данные заказчика"):
            o_page.append_data_customer()
        with allure.step("Нажимаем кнопку 'Далее'"):
            o_page.click_on_button_next()
        with allure.step("Выбираем дату"):
            o_page.choice_data_in_calendar()
        with allure.step("Выбираем срок аренды"):
            o_page.choice_rent_term()
        with allure.step("Нажимаем заказать"):
            o_page.click_on_button_next()
        with allure.step("Подтверждаем заказ"):
            o_page.click_button_yes_on_modal_window()
        with allure.step("Проверяем создание заказа"):
            assert "Заказ оформлен" in o_page.get_text_complete_order_from_modal_window()
        with allure.step("Нажимаем кнопку 'Посмотреть статус'"):
            o_page.click_check_order_status()
        with allure.step("Нажимаем на лого 'Самокат'"):
            o_page.click_logo_scooter()
        with allure.step("Проверяем переход на страницу создания заказа"):
            assert browser.current_url == URL
        with allure.step("Нажимаем на лого 'Яндекс'"):
            o_page.click_logo_yandex()
        with allure.step("Проверяем переход на страницу Дзен"):
            assert browser.current_url == YANDEX_URL

