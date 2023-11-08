import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    driver = browser.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()

        options.add_argument('--user-agent=Chrome/116.0.0.0 Safari/537.36 CDEKMobileApp/iOS/')

        browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
