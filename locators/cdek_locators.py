from selenium.webdriver.common.by import By


class CdekLocators:
    MAIN_IMAGE                      = By.CSS_SELECTOR, '[class="slick-track"]'
    PRODUCT_PAGE_SELECTOR           = By.CLASS_NAME, "product-page-selector"
    PRODUCT_PAGE_SELECTOR_OPTION    = By.CLASS_NAME, "product-page-selector__option"
    PRODUCT_PRICE                   = By.CLASS_NAME, 'title final-your-price__count'
    PRODUCT_HEADER_NAME             = By.CLASS_NAME, 'product-header-name'
    ADD_CART_PRODUCT                = By.CSS_SELECTOR, '[class="ps-btn ps-btn--black add-cart-product"]'
    GO_TO_BASKET                    = By.CSS_SELECTOR, '[class="ps-btn ps-btn--black add-cart-product to-cart"]'
    MAIN_LOGO                     = By.CLASS_NAME, 'cd-header__logo'
    SLIDER = By.XPATH, '//div[@class="owl-item"]/a'
    # SLIDER = By.XPATH, '//*[@id="owl-ps-header-slider"]/div[1]/div/div[8]/a/div/div[1]/div[1]'
    BREND_ITEM = By.CLASS_NAME, 'brend-item'
    EMAIL_BUTTON = By.CLASS_NAME, 'sh-auth-module__form-route'
    EMAIL_INPUT = By.CLASS_NAME, 'sh-control has-icon'
    ABOUT_US = By.CLASS_NAME, 'cd-header__links-item  cd-header__links-item--about-us '
    PAYMENT = By.CLASS_NAME, 'cd-header__links-item  cd-header__links-item--payment '
    SEARCH_FIELD = By.CLASS_NAME, 'ps-form--quick-search'
    INPUT_SEARCH_FIELD = By.CLASS_NAME, 'digi-search-form__input'
    TEXT_INPUT = By.CLASS_NAME, 'digi-search-form__actions'
    PRODUCT_GRID_SEARCH = By.CLASS_NAME, 'digi-product digi-product_ac'

    AUTH_BUTTON = By.ID, 'personal-area-menu'

    CATALOG = By.XPATH, '//*[@id="cd-header__catalog-btn"]'
    CATALOG_PRODUCT = By.XPATH, '//*[@id="cd-header__menu"]/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/a'
    OPLATA = By.XPATH, '//*[@id="cd-header"]/div[1]/div[1]/div/div[1]/div[3]/a'
    ITEM = By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div[7]/div/div'
    BUTTON_CATALOG = By.CLASS_NAME, 'cd-header__cat-ref-item'
    PRODUCT_CATALOG = By.CLASS_NAME, 'ps-product-item__image-product__block'
    PRODUCT_FILTER = By.XPATH, '//*[@id="product-filter-app"]/div/div/div[2]/div[2]/div[1]/div[1]/label/span[1]'

class CartLocators:
    TITLE_CART = By.CLASS_NAME, 'ps-product__content'
    CHECKOUT = By.CSS_SELECTOR, '[class="sh-btn sh-btn-success btn-checkout-order"]'
    PRODUCT_PRICE_CART = By.XPATH, '//div[@class="product__price"]/span'
    TOTAL_PRICE_CART = By.CLASS_NAME, 'total-price-desktop'
    IMAGE_PRODUCT = By.CLASS_NAME, 'ps-product__thumbnail'
    SHOPPING_TOTAL = By.CLASS_NAME, 'ps-block--shopping-total'


class autorization:
    AUTH = By.CLASS_NAME, 'cd-header__navbar-item-wrap'
    EMAIL = By.CLASS_NAME, 'sh-auth-module__form-routes'
    EMAIL_INPUT = By.XPATH, '/html/body/div[6]/div[2]/div/div[2]/div[2]/div/div[2]/div/span'

class ProductPage:
    CURRENT_PRICE = By.CLASS_NAME, 'sh-product-page__main-price-value'
    OLD_PRICE = By.CLASS_NAME, 'sh-product-page__old-price'
    IMAGE_PRODUCT = By.CLASS_NAME, 'slick-slide slick-current slick-active'
