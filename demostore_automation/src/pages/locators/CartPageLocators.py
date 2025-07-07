
from selenium.webdriver.common.by import By

class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.wc-block-cart-items__row td.wc-block-cart-item__product a.wc-block-components-product-name')

    COUPON_FIELD = (By.ID, 'wc-block-components-total-coupon__input-0')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'div.wc-block-components-total-coupon__content button.wc-block-components-button') #need to check

    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.wc-block-cart__submit-button')

    ADD_COUPON_HIDE_SHOW = (By.CSS_SELECTOR, 'div.wc-block-components-totals-wrapper div.wc-block-components-totals-coupon')

    CART_PAGE_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.wc-block-components-notices__snackbar.wc-block-components-notice-banner__content')