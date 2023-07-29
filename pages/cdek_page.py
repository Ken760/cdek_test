from .base_page import BasePage
from locators.cdek_locators import CdekLocators
from time import sleep
from random import random


class CdekPage(BasePage):

    def checking_product(self):
        assert self.is_element_present(*CdekLocators.PRODUCT_PAGE_SELECTOR), "Кнопка выбора размеров отсутствует"
        product_select = self.browser.find_element(*CdekLocators.PRODUCT_PAGE_SELECTOR)
        product_scroll = self.browser.execute_script("arguments[0].scrollIntoView();", product_select)
        product_select.click()

    def get_size(self):
        assert self.is_element_present(*CdekLocators.PRODUCT_PAGE_SELECTOR_OPTION), "Размеры отсутствуют"

        product_select_size = self.browser.find_elements(*CdekLocators.PRODUCT_PAGE_SELECTOR_OPTION)[0].click()

    def check_add_cart(self):
        sleep(2)
        assert self.is_element_present(*CdekLocators.ADD_CART_PRODUCT), 'Кнопка добавить в корзину отсутствует'
        add_cart = self.browser.find_element(*CdekLocators.ADD_CART_PRODUCT).click()

    def go_backet(self):
        assert self.is_element_present(*CdekLocators.GO_TO_BASKET), 'Кнопка перейти в коризну отсутствует'
        go_to_basket = self.browser.find_element(*CdekLocators.GO_TO_BASKET).click()
        sleep(2)


    def backet_checkout(self):
        assert self.is_element_present(*CdekLocators.CHECKOUT), 'Кнопка оформить заказ отсутсвует'
        button_checkout = self.browser.find_element(*CdekLocators.CHECKOUT)
        checkout_scroll = self.browser.execute_script("arguments[0].scrollIntoView();", button_checkout)
        button_checkout.click()
