from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, width, height, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.browser.set_window_size(width, height)
        # self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def go_to_site(self, url):
        return self.browser.get(url)

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser.find_element(how, what), timeout)
        except NoSuchElementException:
            return False
        return True

    def is_elements_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser.find_elements(how, what), timeout)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False