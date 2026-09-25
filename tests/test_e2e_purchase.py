import pytest

from pages.header_page import HeaderPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from test_data.ecommerce_data import PRODUCT_DATA
from utils.constants import BASE_URL


def test_ecommerce_purchase_journey(page, product_name):

    # Get product test data
    if product_name not in PRODUCT_DATA:
        pytest.fail(
            f"Product data not found for: {product_name}"
        )

    data = PRODUCT_DATA[product_name]

    search_product = data["search"]
    expected_product = data["product"]
    pincode = data["pincode"]

    # Create Page Objects
    header = HeaderPage(page)
    product = ProductPage(page)

    # 1. Open Homepage
    page.goto(
        BASE_URL,
        wait_until="domcontentloaded"
    )

    # 2. Search Product
    header.search_product(search_product)

    # 3. Open Product from Search Result
    product.open_product(expected_product)

    # 4. Get Actual Product Name from PDP
    actual_product = product.get_product_name()

    # 5. Verify Product Name
    assert actual_product == expected_product, (
        f"Expected product: {expected_product}, "
        f"Actual product: {actual_product}"
    )

    print(f"Expected Product: {expected_product}")
    print(f"Actual Product: {actual_product}")

    # 6. Check Add to Cart availability
    is_available = product.is_product_available()

    print(f"Add to Cart Enabled: {is_available}")

    # Stop test if product is unavailable
    if not is_available:
        print(
            f"Product '{actual_product}' "
            "is not available for Add to Cart"
        )
        return

    # 7. Add Product to Cart
    product.add_product_to_cart()

    # 8. Create Cart Page Object
    cart = CartPage(page)

    # 9. Verify Product in Cart
    cart.verify_product(actual_product)

    # 10. Enter Pincode
    cart.enter_pincode(pincode)

    # 11. Proceed to Checkout
    cart.proceed_to_checkout()