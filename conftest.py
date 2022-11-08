import pytest

from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser, base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser, base_url)
    fixture.session.ensure_login(username="admin", password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def after_all(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(final)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption(
        "--base_url", action="store", default="http://localhost/addressbook/"
    )
    parser.addoption("--password", action="store", default="")
