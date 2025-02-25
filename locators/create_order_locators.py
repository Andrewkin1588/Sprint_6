from selenium.webdriver.common.by import By


class CreateOrderLocators:
    CREATE_ORDER_MAIN_PAGE_HEADER = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']"]
    CREATE_ORDER_MAIN_PAGE_FOOTER = [By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM"]
    INPUT_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    INPUT_LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    INPUT_STATION = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    INPUT_PHONE_NUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    BUTTON_CHECK_STATUS = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(text(),'Посмотреть статус')]"]
    INPUT_DATE_ORDER = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    DROPDOWN_RENT_TERM = [By.XPATH, "//div[@class='Dropdown-control']"]
    SELECT_RENT_TERM = [By.XPATH, "//div[@class='Dropdown-option'][contains(text(),'сутки')]"]
    BUTTON_YES_POPUP = [By.XPATH, "//button[contains(text(),'Да')]"]
    TEXT_COMPLETED_ORDER = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    LINK_SCOOTER_LOGO = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    LINK_YANDEX_LOGO = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    CALENDAR_DATA = [By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--028']"]

