

import pytest
import logging as logger

from demostore_automation.src.pages.ProductPage import ProductPage #imported it now create object for it

@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVariableProduct:

@pytest.fixture(scope='class')
def setup(self, request):
       
    #find (via API) or hardcode a variable product
       product_slug = "product/hoodie/"
       expected_name = "Hoodie"


       #need to go to the product page (need a function)
       product_page = ProductPage(self.driver) #object and because we created the object the constructor (__init__) gets executed & because it has parameter we must pass a parameter here in parathesis
       product_page.go_to_product_page(product_slug) #must pass argument because we added one in ProductPage.py file
    
    
    @pytest.mark.des22 #matches in qase.io
    def test_variable_product_page_verify_product_name(self): #self added because it's a class
       logger.info('Running test: test_variable_product_page_verify_prod')


   

       #need to get the displayed name
       displayed_name = product_page.get_displayed_product_name()

       #verify the name is what is expected
       assert expected_name == displayed_name, f"Unexpected name displayed for a variable product. "\ 
                  f"Expected: {expected_name}, Displayed: {displayed_name}"




