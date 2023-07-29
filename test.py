
from pages.cdek_page import CdekPage
# from pages.size_page import
import allure
import pytest

@allure.title("")
def test_cdek_1024_1366(browser):
    cdek = CdekPage(browser)
    with allure.step("Проверка открытия карточки"):
        cdek.go_to_site('https://cdek.shopping/p/54588/krossovki-nike-sportswear-wmns-air-force-1-07-white')
    with allure.step("Проверка кнопки выбора размеров"):
        cdek.checking_product()

    with allure.step('Проверка появившихся размеров'):
        cdek.get_size()
    with allure.step('Проверка добавления в карзину'):
        cdek.check_add_cart()
    with allure.step('Проверка кнопки перехода в карзину'):
        cdek.go_backet()
    with allure.step('Проверка кнопки купить'):
        cdek.backet_checkout()


# @allure.title("")
# def test_cdek_360_1366(browser):
#     cdek = CdekPage(browser, width=360, height=640)
#     with allure.step("Проверка открытия карточки"):
#         cdek.go_to_site('https://cdek.shopping/p/54588/krossovki-nike-sportswear-wmns-air-force-1-07-white')
#     with allure.step("Проверка кнопки выбора размеров"):
#         cdek.checking_product()
#
#     with allure.step('Проверка появившихся размеров'):
#         cdek.get_size()
#     with allure.step('Проверка добавления в карзину'):
#         cdek.check_add_cart()
#     with allure.step('Проверка кнопки перехода в карзину'):
#         cdek.go_backet()
#     with allure.step('Проверка кнопки купить'):
#         cdek.backet_checkout()


# @allure.title("")
# def test_cdek_(browser):
#     cdek = browser.set_window_size(600, 1024)
#     cdek.go_to_site('https://cdek.shopping/')
#
#
# @allure.title("")
# def test_cdek_(browser):
#     cdek = browser.set_window_size(601, 962)
#     cdek.go_to_site('https://cdek.shopping/')
#
#
# @allure.title("")
# def test_cdek_(browser):
#     cdek = browser.set_window_size(800, 1280)
#     cdek.go_to_site('https://cdek.shopping/')

#
# @allure.title("")
# def test_cdek_(browser):
#     cdek = browser.set_window_size(1280, 800)
#     cdek.go_to_site('https://cdek.shopping/')
#
#
# @allure.title("")
# def test_cdek_(browser):
#     cdek = browser.set_window_size(1366, 768)
#     cdek.go_to_site('https://cdek.shopping/')