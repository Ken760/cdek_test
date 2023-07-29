from selenium.webdriver import ActionChains

from .base_page import BasePage
from locators.cdek_locators import CdekLocators
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
        sleep(2)

    def backet_checkout(self):
        assert self.is_element_present(*CdekLocators.CHECKOUT), 'Кнопка оформить заказ отсутсвует'
        try:
            button_checkout = self.browser.find_element(*CdekLocators.CHECKOUT)
            sleep(1)
            button_checkout.click()
        except:
            button_checkout = self.browser.find_element(*CdekLocators.CHECKOUT)
            self.browser.execute_script("arguments[0].scrollIntoView(true);", button_checkout)
            sleep(2)
            button_checkout.click()
