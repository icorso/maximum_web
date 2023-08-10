import allure
from selenium.webdriver.common.by import By

from pages.base_page import HtmlPage


class MainPage(HtmlPage):

    @property
    def breadcrumb_username(self):
        return self.find_element(By.CSS_SELECTOR, "ol>li[class*='active']>a")

    @property
    def settings_menu_button(self):
        return self.find_element(By.CSS_SELECTOR, "button>span[class='nav-link']")

    @property
    def settings_menu(self):
        return self.find_element(By.CLASS_NAME, "dropdown-menu.dropdown-menu-right.show")

    @allure.step("Выбирает пункт {item_name} из меню настроек")
    def settings_menu_select_by_name(self, item_name: str):
        menu_items = self.settings_menu.find_elements(By.TAG_NAME, 'a')
        menu_item = [i for i in menu_items if i.text == item_name]
        if len(menu_item) > 1:
            print(f'Пунктов меню с именем {item_name} больше одного. Будет выбран первый.')
        assert len(menu_item) >= 1, f'Пункт меню {item_name} не найден'
        menu_item[0].click()
