

import pytest
import logging as logger

from demostore_automation.src.pages.ProductPage import ProductPage #imported it now create object for it
from demostore_automation.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper

@pytest.mark.usefixtures("init_driver")
class TestProductDetailPageVariableProduct:

   @pytest.fixture(scope='class')
   def setup(self, request):
       
    #find (via API) or hardcode a variable product
       product_slug = "product/hoodie/"
       request.cls.expected_name = "Hoodie"
       request.cls.expected_url = ['/wp-content/uploads/2024/10/hoodie-2-416x416.jpg']

       #make api call to get details of the product
       product_api_helper = ProductsAPIHelper()
       product_info = product_api_helper.call_get_product_by_id(self.product_id)
       images = product_info['images']

      request.cls.all_expected_urls = [image.get('src') for image in images]  

       #need to go to the product page (need a function)
       product_page = ProductPage(self.driver) #object and because we created the object the constructor (__init__) gets executed & because it has parameter we must pass a parameter here in parathesis
       product_page.go_to_product_page(product_slug) #must pass argument because we added one in ProductPage.py file
    
    
@pytest.mark.des22 #matches in qase.io
def test_variable_product_page_verify_product_name(self): #self added because it's a class
       logger.info('Running test: test_variable_product_page_verify_prod')


   

       #need to get the displayed name
       displayed_name = product_page.get_displayed_product_name()

       #verify the name is what is expected
       assert expected_name == displayed_name, f"Unexpected name displayed for a variable product. Expected: {expected_name}, Displayed: {displayed_name}"



@pytest.mark.des23
def test_variable_product_page_verify_main_image(self, setup):
      logger.info("Running test: test_variable_product_page_verify_main_image")
      displayed_img_url = self.product_page.get_url_of_displayed_main_image()
      logger.info(f"Displayed image url is: {displayed_img_url}")

      #verify it is a valid url
      assert displayed_img_url.startswith('http'), "the url did not start with http"
      assert displayed_img_url.endswith('jpg'), "ther url did not end with jpg"

      assert displayed_img_url.endswith(self.expected_url), f"Expected and displayed url do not match. " \
                                  f"Expected: {self.expected_url}, Displayed: {displayed_img_url}"
      


      @pytest.mark.des24
      def test_variable_product_page_verify_extra_images(self, setup):
           logger.info("Running test: test_variable_product_page_verify_extra_images")

           all_displayed_urls = self.product_page.get_url_of_displayed_alternate_images()

           assert all_displayed_urls.sort() == self.all_expected_urls.sort(), "The expected and displayed alternate images urls do not match."





#verify product type test on product page
@pytest.mark.des25
def test_variable_product_page_verify_product_type_text(self, setup):
     logger.info("Running test: test_variable_product_page_verify_product_type_text")

product_type_text = self.product_page.get_product_type_text()
assert product_type_text == 'This is a variable product.', f"Unexpected product type text on page." \
                                                           f"Expected: 'This is a variable prodcut.'" \
                                                           f"Actual: '{product_type_text}'"



#verify product price range - 
@pytest.mark.des26
def test_variable_product_page_verify_price_range_before_option_selection(self, setup):
     """
     Test method to verify the price range displayed on a variable product page before any option selection.

     Args:
         setup: A setup object 
     """

   price_html = self.product_page.get_displayed_product_price()
   api_price_string = convert_html_to_text(self.product_api_data['price_html'])     
   assert price_html == api_price_string, f"Expected price_html = {api_price_string}," \
                                          f"Actual: {price_html}"            



























