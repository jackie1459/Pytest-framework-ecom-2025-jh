

from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended #importing the folder.thefile
from demostore_automation.src.configs.MainConfigs import MainConfigs #getting the base URL
from demostore_automation.src.pages.locators.ProductPageLocators import ProductPageLocators


class ProductPage(ProductPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver) #self makes it available on every function within the class


    def go_to_product_page(self, product_slug):

        base_url = MainConfigs.get_base_url()
        product_url = f"{base_url}/{product_slug}" #is the same as product_url = base_url + "/" + product_slug
        self.sl.go_to(product_url)

    def get_displayed_product_name(self):
       return self.sl.wait_and_get_text(self.PRODUCT_TITLE)
      # SAME as above displayed_text = self.sl.wait_and_get_text(self.PRODUCT_TITLE)
       #return displayed_text
    







