from dataclasses import make_dataclass

import pytest

from driver import get_driver, close_driver
from pages.login import LoginPage
from pages.main import MainPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    close_driver()


@pytest.fixture
def pages():
    pages = make_dataclass("pages", [])
    pages.login = LoginPage()
    pages.main = MainPage()
    return pages
