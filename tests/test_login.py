import allure


def test_incorrect_login_attempt(driver, pages):
    pages.login.open()
    pages.login.authorize("test", "test")
    with allure.step("Проверяет сообщение о некорректном логине"):
        assert "Login failed - Please try again" in pages.login.error_message.text
