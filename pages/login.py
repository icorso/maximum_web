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

    @allure.step("В")
    def authorize(self, username=settings.username, password=settings.password):
        self.login_field.clear()
        self.login_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.submit.click()
