import allure
from selenium.webdriver.common.by import By

import settings
from pages.base_page import HtmlPage


class LoginPage(HtmlPage):
    def __init__(self, url=settings.url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    @property
    def header(self):
        return self.find_element(By.TAG_NAME, 'h2')

    @property
    def login_field(self):
        return self.find_element(By.CSS_SELECTOR, '[name*=username]')

    @property
    def password_field(self):
        return self.find_element(By.CSS_SELECTOR, '[name*=password')

    @property
    def submit(self):
        return self.find_element(By.TAG_NAME, 'button')

    @property
    def error_message(self):
        return self.find_element(By.CLASS_NAME, 'alert.alert-danger.text-center')

    @allure.step("Авторизует пользователя {username} / {password}")
    def authorize(self, username=settings.username, password=settings.password):
        self.login_field.clear()
        self.login_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.submit.click()

    @allure.step("Название страницы соответствует {header}")
    def has_header(self, header: str):
        assert self.header.text == header, "Заголовок страницы не соответствует ожидаемому"

    @allure.step("Текст ошибки авторизации содержит {error_text}")
    def has_auth_error(self, error_text: str):
        assert error_text in self.error_message.text, "Некорректное сообщение об ошибке"

