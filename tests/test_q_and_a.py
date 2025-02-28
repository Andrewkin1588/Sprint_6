import allure
import pytest
from constants import URL
from locators.q_and_a_locators import *
from pages.main_page import MainPage

extended_answer = [
    (Questions.Q_HOW_MUCH, Answers.A_HOW_MUCH, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (Questions.Q_FEW_BIKE, Answers.A_FEW_BIKE,
     "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (Questions.Q_RENT_TIME, Answers.A_RENT_TIME,
     "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (Questions.Q_TODAY_ORDER, Answers.A_TODAY_ORDER,
     "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (Questions.Q_BE_BACK_BIKE, Answers.A_BE_BACK_BIKE,
     "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (Questions.Q_CHARGING_BIKE, Answers.A_CHARGING_BIKE,
     "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (Questions.Q_CANCEL_ORDER, Answers.A_CANCEL_ORDER,
     "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (Questions.Q_LIV_MCAD, Answers.A_LIV_MCAD, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
]


class TestQuestionsAndAnswers:

    @pytest.mark.parametrize('question,answer,extended', extended_answer)
    def test_question_and_answer(self, question, answer, extended, browser):
        with allure.step("Переходим на главную страницу"):
            browser.get(URL)
        m_page = MainPage(browser)
        m_page.sleep_while_not_located_faq_div()
        with allure.step("Нажимаем на вопрос"):
            m_page.click_question(question)
        with allure.step("Сравниваем ответ на вопрос"):
            assert m_page.get_text_answer(answer) == extended
