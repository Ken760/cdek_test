from pages.cdek_page import CdekPage
# from pages.size_page import
import allure
import pytest


@allure.title("проверка на разрешении 1366×768")
def test_resolutin_one(browser):
    go_test_cdek(browser, width=1366, height=768)


@allure.title("проверка на разрешении 1920×1080")
def test_resolution_two(browser):
    go_test_cdek(browser, width=1920, height=1080)


@allure.title("проверка на разрешении 1536×864")
def test_resolution_three(browser):
    go_test_cdek(browser, width=1536, height=864)


@allure.title("проверка на разрешении 1440×900")
def test_resolution_four(browser):
    go_test_cdek(browser, width=1440, height=900)


@allure.title("проверка на разрешении 1280×720")
def test_resolution_five(browser):
    go_test_cdek(browser, width=1280, height=720)


@allure.title("проверка на разрешении 640×480")
def test_resolution_six(browser):
    go_test_cdek(browser, width=640, height=480)


@allure.title("проверка на разрешении 375×667")
def test_resolution_seven(browser):
    go_test_cdek(browser, width=375, height=667)


@allure.title("проверка на разрешении 414×896")
def test_resolution_eight(browser):
    go_test_cdek(browser, width=414, height=896)


@allure.title("проверка на разрешении 360×760")
def test_resolution_nine(browser):
    go_test_cdek(browser, width=360, height=760)


@allure.title("проверка на разрешении 414×736")
def test_resolution_ten(browser):
    go_test_cdek(browser, width=414, height=736)


@allure.title("проверка на разрешении 768×1024")
def test_resolution_eleven(browser):
    go_test_cdek(browser, width=768, height=1024)


@allure.title("проверка на разрешении 1280×800")
def test_resolution_twelve(browser):
    go_test_cdek(browser, width=1280, height=800)


@allure.title("проверка на разрешении 800×1280")
def test_resolution_thirteen(browser):
    go_test_cdek(browser, width=800, height=1280)

@allure.title("проверка на разрешении 601×962")
def test_resolution_fourtenn(browser):
    go_test_cdek(browser, width=601, height=962)


@allure.title("проверка на разрешении 600×1024")
def test_resolution_fiveteen(browser):
    go_test_cdek(browser, width=600, height=1024)


@allure.title("проверка на разрешении 1024×1366")
def test_resolution_sixteen(browser):
    go_test_cdek(browser, width=1024, height=1366)


def go_test_cdek(browser, width, height):
    cdek = CdekPage(browser, width, height)
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
