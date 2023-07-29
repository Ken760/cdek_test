from selenium.webdriver.common.by import By


class CdekLocators:
    MAIN_IMAGE                      = By.CSS_SELECTOR, '[class="slick-track"]'
    PRODUCT_PAGE_SELECTOR           = By.CLASS_NAME, "product-page-selector"
    PRODUCT_PAGE_SELECTOR_OPTION    = By.CLASS_NAME, "product-page-selector__option"
    PRODUCT_PRICE = By.CLASS_NAME, 'title final-your-price__count'
    PRODUCT_HEADER_NAME = By.CLASS_NAME, 'product-header-name'
    ADD_CART_PRODUCT = By.CSS_SELECTOR, '[class="ps-btn ps-btn--black add-cart-product"]'
    GO_TO_BASKET = By.CSS_SELECTOR, '[class="ps-btn ps-btn--black add-cart-product to-cart"]'
    CHECKOUT = By.CSS_SELECTOR, '[class="sh-btn sh-btn-success btn-checkout-order"]'