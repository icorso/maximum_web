import allure

from driver import get_driver


class HtmlPage(object):
    def __init__(self, driver=None, url=None):
        if url:
            self.url = url
        self.__driver = driver if driver else get_driver()

    @property
    def _driver(self):
        if self.__driver:
            return self.__driver
        return get_driver()

    @allure.step("Открывает url")
    def open(self):
        if not self.url:
            raise Exception('Параметр url не задан')
        self.__driver.get(self.url)

    def find_element(self, *args):
        return self.__driver.find_element(*args)

    def find_elements(self, *args):
        return self.__driver.find_elements(*args)

    def implicitly_wait(self, *args):
        return self.__driver.implicitly_wait(*args)
