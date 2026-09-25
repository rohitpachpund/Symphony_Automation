from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # Cart Product
        self.product_title = page.locator(
            "h3.product_title.m-0"
        ).first

        # Cart Pincode
        self.pincode_input = page.locator(
            "#cart-pincode-input"
        )

        # Cart Checkout
        # Select only visible checkout button
        self.checkout = page.locator(
            'button[name="checkout"]:visible'
        ).first

    def verify_product(self, expected_product):

        expect(
            self.product_title
        ).to_be_visible(timeout=10000)

        expect(
            self.product_title
        ).to_contain_text(expected_product)

    def enter_pincode(self, pincode):

        expect(
            self.pincode_input
        ).to_be_visible(timeout=10000)

        self.pincode_input.scroll_into_view_if_needed()

        self.pincode_input.fill(
            pincode,
            force=True
        )

    def proceed_to_checkout(self):

        # Wait for checkout button to become visible
        expect(
            self.checkout
        ).to_be_visible(timeout=15000)

        # Wait until checkout is enabled
        expect(
            self.checkout
        ).to_be_enabled(timeout=15000)

        self.checkout.scroll_into_view_if_needed()

        self.checkout.click()