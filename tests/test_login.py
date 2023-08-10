import allure


def test_login_page_open(pages):
    pages.login.open()
    pages.login.has_header('Login')


def test_incorrect_login_attempt(pages):
    pages.login.open()
    pages.login.authorize("test", "test")
    pages.login.has_auth_error("Login failed - Please try again")


def test_successful_login(pages):
    pages.login.open()
    pages.login.authorize()
    with allure.step("Проверяет имя пользователя на главной странице после входа"):
        assert pages.main.breadcrumb_username.text == "Guest, Joe O (guest) - Home", \
            "Некорректный пользователь на главной странице"


def test_successful_logoff(pages):
    pages.login.open()
    pages.login.authorize()
    pages.main.settings_menu_button.click()
    pages.main.settings_menu_select_by_name('Logoff guest')
    pages.login.has_header('Login')
