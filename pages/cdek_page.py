from selenium.webdriver import ActionChains
from .base_page import BasePage
from locators.cdek_locators import CdekLocators, CartLocators, autorization
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import random
from selenium.webdriver.common.action_chains import ActionChains


class CdekPage(BasePage):

    def checking_product(self):
        assert self.is_element_present(*CdekLocators.PRODUCT_PAGE_SELECTOR), "Кнопка выбора размеров отсутствует"
        try:
            product_select = self.browser.find_element(*CdekLocators.PRODUCT_PAGE_SELECTOR)
            product_select.click()
        except:
            product_select = self.browser.find_element(*CdekLocators.PRODUCT_PAGE_SELECTOR)

            self.browser.execute_script("arguments[0].scrollIntoView(true);", product_select)
            product_select.click()

    def get_size(self):
        assert self.is_element_present(*CdekLocators.PRODUCT_PAGE_SELECTOR_OPTION), "Размеры отсутствуют"
        product_select_size = self.browser.find_elements(*CdekLocators.PRODUCT_PAGE_SELECTOR_OPTION)[0].click()

    def check_add_cart(self):
        assert self.is_element_present(*CdekLocators.ADD_CART_PRODUCT), 'Кнопка добавить в корзину отсутствует'
        add_cart = self.browser.find_element(*CdekLocators.ADD_CART_PRODUCT).click()

    def go_backet(self):
        assert self.is_element_present(*CdekLocators.GO_TO_BASKET), 'Кнопка перейти в коризну отсутствует'
        go_to_basket = self.browser.find_element(*CdekLocators.GO_TO_BASKET).click()
        sleep(5)

    def backet_checkout(self):
        assert self.is_element_present(*CartLocators.CHECKOUT), 'Кнопка оформить заказ отсутсвует'
        try:
            button_checkout = self.browser.find_element(*CartLocators.CHECKOUT)
            sleep(1)
            button_checkout.click()
        except:
            button_checkout = self.browser.find_element(*CartLocators.CHECKOUT)
            self.browser.execute_script("arguments[0].scrollIntoView(true);", button_checkout)
            sleep(2)
            button_checkout.click()

    def test_cattalog_button(self):
        cattalog_button = self.browser.find_elements(*CdekLocators.SLIDER)[-1]
        # assert cattalog_button, 'Кнопка каталога отсутствует'
        cattalog_button.click()
        sleep(5)

    def search_field(self):
        assert self.is_element_present(*CdekLocators.SEARCH_FIELD), 'Поле поиска отутсвует'
        search = self.browser.find_element(*CdekLocators.SEARCH_FIELD)
        search.click()

    # def input_search_field(self):
    #     input_search = self.browser.find_element(*CdekLocators.INPUT_SEARCH_FIELD).click()
    #     sleep(5)
    #     input_search.clear()
    #     input_search.send_keys('aaa')
    def home_button(self):
        buttons = self.browser.find_element(*CdekLocators.AUTH_BUTTON)
        buttons.click()
        sleep(5)

    def auth(self):
        auth_button = self.browser.find_elements(*autorization.AUTH)[1]
        auth_button.click()
        email_button = self.browser.find_element(*autorization.EMAIL)
        email_button.click()
        sleep(5)
        email_input = self.browser.find_element(*autorization.EMAIL_INPUT)
        email_input.click()
        email_input.send_keys('aaaaa')
        sleep(5)



        # email_input.send_keys('nehnaev@gmail.com')
        #
        # sleep(10)
        # sleep(1000)
    def slider(self):
        assert self.is_element_present(*CdekLocators.SLIDER), 'Банер отсутсвует'
        slider_click = self.browser.find_element(*CdekLocators.SLIDER)
        slider_click.click()
        sleep(500)

    def catalog(self):
        # assert self.is_element_present(*CdekLocators.CATALOG), 'Кнопка каталог отсутсвует или не работает'
        catalog = self.browser.find_element(*CdekLocators.CATALOG)
        sleep(10)
        catalog.click()
        sleep(10)
        catalog_product = self.browser.find_element(*CdekLocators.CATALOG_PRODUCT)
        sleep(5)
        catalog_product.click()
        sleep(20)

    def item(self):
        assert self.is_element_present(*CdekLocators.ITEM), 'Товар отсутсвует'
        item_click = self.browser.find_element(*CdekLocators.ITEM)
        item_click.click()
        sleep(5)

    def catalog_laptop(self):
        laptop_button = self.browser.find_elements(*CdekLocators.BUTTON_CATALOG)[1]
        laptop_button.click()
        sleep(5)
        product_catalog = self.browser.find_elements(*CdekLocators.PRODUCT_CATALOG)[0]
        product_catalog.click()
        sleep(5)

    def catalog_filter(self):
        laptop_button = self.browser.find_elements(*CdekLocators.BUTTON_CATALOG)[1]
        laptop_button.click()
        sleep(5)
        filter_catalog = self.browser.find_element(*CdekLocators.PRODUCT_FILTER)
        filter_catalog.click()
        sleep(10)
    def catalog_gaming(self):
        laptop_button = self.browser.find_elements(*CdekLocators.BUTTON_CATALOG)[0]
        laptop_button.click()
        product_catalog = self.browser.find_elements(*CdekLocators.PRODUCT_CATALOG)[0]
        product_catalog.click()
        sleep(5)

