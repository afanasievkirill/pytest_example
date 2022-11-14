import json
import jsonpickle
import os.path
import pytest
import importlib


from fixture.application import Application
from generator.group import generate_group_data
from generator.contact import generate_contact_data

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
        generate_group_data()
        generate_contact_data()
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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            ddt = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, ddt, ids=[str(x) for x in ddt])
        elif fixture.startswith("json_"):
            ddt = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, ddt, ids=[str(x) for x in ddt])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).ddt


def load_from_json(file):
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file),
        encoding="utf-8",
    ) as f:
        return jsonpickle.decode(f.read())
