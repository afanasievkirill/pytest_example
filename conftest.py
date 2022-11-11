import json
import os.path
import pytest


from fixture.application import Application

fixture = None
config = None


@pytest.fixture
def app(request):
    """
        Фикстура для подготовки окружения тестов.
    Args:
        request:
    Returns:
        fixture: Application : экземпляр класса Application fixture/application.py
    """
    global fixture
    global config
    browser = request.config.getoption("--browser")
    config_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--config")
    )
    if config is None:
        with open(config_file_path, encoding="utf-8") as config_file:
            config = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, base_url=config["base_url"])
    fixture.session.ensure_login(username=config["login"], password=config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def after_all(request):
    """
        Фикстура для заврешения сессии после окончания прогона.
    Args:
        request:
    """

    def final():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture


def pytest_addoption(parser):
    """
        Функция описания опций фикстуры
    Args:
        parser:
    """
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--config", action="store", default="config.json")
