
from demostore_automation.src.utilities.wooAPIUtility import WooAPIUtility


class ProductsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_get_product_by_id(self, product_id):
        return self.woo_api_utility.get(f"products/{product_id}", expected_status_code=200)
    
    def call_create_product(self):
        self.woo_api_utility.post('products', params=payload, expected_status_code=201)













