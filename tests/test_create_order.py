import time

import allure
import pytest

from locators.create_order_locators import CreateOrderLocators
from pages.base_page import BasePage
from constants import URL
from pages.order_page import OrderPage
from tests.conftest import teardown_browser


class TestCreateOrder:
    def test_create_order(self, browser):
        allure.step("Переходим на главную страницу")
        browser.get(URL)
        b_page = BasePage(browser)
        o_page = OrderPage(browser)
        allure.step("Нажимаем на кнопку 'Заказать'")
        b_page.click_on_create_order_main_page()
        allure.step("Заполняем данные заказчика")
        o_page.send_keys(CreateOrderLocators.INPUT_NAME, 'Тест')
        o_page.send_keys(CreateOrderLocators.INPUT_LAST_NAME, 'Тестов')
        o_page.send_keys(CreateOrderLocators.INPUT_ADDRESS, 'Тестовая')
        o_page.send_keys(CreateOrderLocators.INPUT_PHONE_NUMBER, '89099999999')
        o_page.select_option()
        allure.step("Нажимаем кнопку 'Далее'")
        o_page.button_click(CreateOrderLocators.BUTTON_NEXT)
        allure.step("Выбираем дату")
        o_page.button_click(CreateOrderLocators.INPUT_DATE_ORDER)
        o_page.button_click(CreateOrderLocators.CALENDAR_DATA)
        allure.step("Выбираем срок аренды")
        o_page.button_click(CreateOrderLocators.DROPDOWN_RENT_TERM)
        o_page.button_click(CreateOrderLocators.SELECT_RENT_TERM)
        allure.step("Нажимаем заказать")
        o_page.button_click(CreateOrderLocators.BUTTON_NEXT)
        allure.step("Подтверждаем заказ")
        o_page.button_click(CreateOrderLocators.BUTTON_YES_POPUP)
        allure.step("Проверяем создание заказа")
        assert "Заказ оформлен" in o_page.get_text(CreateOrderLocators.TEXT_COMPLETED_ORDER)
        allure.step("Нажимаем кнопку 'Посмотреть статус'")
        o_page.button_click(CreateOrderLocators.BUTTON_CHECK_STATUS)
        allure.step("Нажимаем на лого 'Самокат'")
        o_page.button_click(CreateOrderLocators.LINK_SCOOTER_LOGO)
        allure.step("Проверяем переход на страницу создания заказа")
        assert browser.current_url == 'https://qa-scooter.praktikum-services.ru/'
        allure.step("Нажимаем на лого 'Яндекс'")
        o_page.button_click(CreateOrderLocators.LINK_YANDEX_LOGO)
        allure.step("Проверяем переход на страницу Дзен")
        b_page.wait_redirect_url('https://dzen.ru/?yredirect=true')
        assert browser.current_url == 'https://dzen.ru/?yredirect=true'
        teardown_browser(browser)

