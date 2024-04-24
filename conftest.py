import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="session")
# def browser():
#     # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
#     # driver = browser.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver
#     driver.quit()


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
        # options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 CDEKMobileApp/iOS/')

        # options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument("--disable-extensions")
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_argument("--disable-blink-features")
        # options.add_argument('--headless')
        options.add_argument('--user-agent=Chrome/116.0.0.0 Safari/537.36 CDEKMobileApp/iOS/')
        # options.add_argument("start-maximized")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)


        browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
