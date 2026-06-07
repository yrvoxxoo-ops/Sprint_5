from selenium.webdriver.common.by import By

class Locators:
    #Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")

    #Кнопка "Личный Кабинет" в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    #Ссылка "Зарегистрироваться" на странице входа
    REGISTRATION_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

    #Ссылка "Войти" на странице регистрации
    LOGIN_LINK_REGISTRATION_PAGE = (By.XPATH, "//a[text()='Войти']")

    #Ссылка "Восстановить пароль" на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    #Поле ввода имени на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    #Поле ввода email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    #Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    #Кнопка "Зарегистрироваться" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    #Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    #Кнопка "Конструктор" в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")

    #Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    #Вкладка "Булки" в конструкторе
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")

    #Вкладка "Соусы" в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")

    #Вкладка "Начинки" в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    #Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//a[@href='/']")

    # Сообщение об ошибке некорректного пароля
    INVALID_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")