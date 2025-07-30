
import pytest
import logging as logger

from demostore_automation.src.utilities.genericUtilities import generate_random_coupon_code
from demostore_automation.src.api_helpers.CouponAPIHelper import CouponAPIHelper


pytestmark = [pytest.mark.coupon_api]

@pytest.fixture(scope='module')
def my_setup():

    #create the helper object in the fixture
    coupon_api_helper = CouponAPIHelper()

    info = {}
    info['coupon_api_helper'] = coupon_api_helper

    return info


@pytest.mark.des30
def test_create_coupon_invalid_discount_type(my_setup):
    logger.info("Running test: test_create_coupon_invalid_discount_type")

    coupon_api_helper = my_setup['coupon_api_helper']


 #create payload
    #need to generate random string everytime since we can only create one coupon per coupon code
    coupon_code = generate_random_coupon_code()
    amount = '50.00'
    discount_type = 'free_cart' 
    payload = {
                "code": coupon_code,
                "discount type": discount_type,
                 "amount": amount
            }

    logger.debug(f"Creating coupon with payload: {payload}")

    #make the call
    response = coupon_api_helper.call_create_coupon(payload, expected_status_code=400)

    expected_failure_response = {
        "code": "rest_invalid_param",
        "message": "Invalid parameter(s): discount_type",
        "data": {
            "status": 400,
            "params": {
                "discount_type": "discount_type is not one of the percent, fixed_cart, and fixed_product."
            },
            "details": {
                "discount_type": {
                    "code": "rest_not_in_enum",
                    "message": "discount_type is not one of the percent, fixed_cart, and fixed_product.",
                    "data": None
                }
            }
        }
    }

    assert response == expected_failure_response, f"Create coupon with invalis discount_type, returned unexpected error body."
    f"Expected: {expected_failure_response}, Actual: {response}"


@pytest.mark.parametrize("discount_type",
                         [
                             pytest.param('percent', marks=[pytest.mark.des27]),
                             pytest.param('fixed_cart', marks=[pytest.mark.des28]),
                             pytest.param('fixed_product', marks=[pytest.mark.des29]),
                             pytest.param(None, marks=[pytest.mark.des31]),
                         ])

def test_create_coupon_discount_type(my_setup, discount_type):

    logger.info(f"Running test: test_create_coupon_discount_type{discount_type}")
    coupon_api_helper = my_setup['coupon_api_helper']


    #create payload
    #need to generate random string everytime since we can only create one coupon per coupon code
    coupon_code = generate_random_coupon_code()
    amount = '100.00'
    expected_discount_type = discount_type if discount_type else "fixed_cart"




    payload = {}
    payload['code'] = coupon_code
    payload['amount'] = amount
    if discount_type:
        payload['discount_type'] = discount_type

    
    logger.debug(f"Creating coupon with payload: {payload}")

    #make the call
    response = coupon_api_helper.call_create_coupon(payload)


    #verify the response, verify id is there, verify the discount_type in the response
    #first verify the id is not null
    assert response ['id'], f"After making create coupon api call, response does not have valid ID."


    #verify the coupon code in the response matches the one in the request
    assert response['code'] == coupon_code.lower, f"'Create coupon' api call mismatched 'code' in request and response. In request: {coupon_code.lower}, in the response {response['code']}"

    #verify the amount
    assert response ['amount'] == amount, f'Create coupon api, amount does not match. Expected: {amount}, Actual: {response['amount']}'

    #verify discount type
    assert response['discount_type'] == discount_type, f"Create coupon api, 'discount_type'does not match. Expected: {discount_type}, Actual: {response['discount_type']}'"

    #verify the data is persistent by making get api call (or going to database)
    #make a GET Coupon call
    coupon_id = response['id']
    get_response = coupon_api_helper.call_retrieve_coupon(coupon_id)
        #verify discount type
    assert response['discount_type'] == discount_type, f"Create coupon api, 'discount_type'does not match. Expected: {discount_type}, Actual: {response['discount_type']}'"





