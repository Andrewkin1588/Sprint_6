from selenium.webdriver.common.by import By


class Questions:
    Q_LISTS = [By.CLASS_NAME, 'accordion__item']
    Q_HOW_MUCH = [By.ID, 'accordion__heading-0']
    Q_FEW_BIKE = [By.ID, 'accordion__heading-1']
    Q_RENT_TIME = [By.ID, 'accordion__heading-2']
    Q_TODAY_ORDER = [By.ID, 'accordion__heading-3']
    Q_BE_BACK_BIKE = [By.ID, 'accordion__heading-4']
    Q_CHARGING_BIKE = [By.ID, 'accordion__heading-5']
    Q_CANCEL_ORDER = [By.ID, 'accordion__heading-6']
    Q_LIV_MCAD = [By.ID, 'accordion__heading-7']


class Answers:
    A_HOW_MUCH = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    A_FEW_BIKE = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    A_RENT_TIME = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    A_TODAY_ORDER = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    A_BE_BACK_BIKE = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    A_CHARGING_BIKE = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    A_CANCEL_ORDER = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    A_LIV_MCAD = [By.XPATH, '//div[@id="accordion__panel-7"]/p']
