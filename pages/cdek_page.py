from selenium.webdriver import ActionChains

from .base_page import BasePage
from locators.cdek_locators import CdekLocators, CartLocators
from time import sleep
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
        sleep(1)

    def input_search_field(self):
        input_search = self.browser.find_element(*CdekLocators.INPUT_SEARCH_FIELD).click()
        sleep(5)
        input_search.send_keys('word')
        sleep(5)



