from playwright.sync_api import Page, expect


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        # Product Title
        # Website has duplicate product titles.
        # We need the visible one.
        self.product_title = page.locator(
            "h1.pdp-title:visible"
        ).first

        # Add to Cart
        self.add_to_cart = page.locator(
            "#stickyAddToCartBtn"
        )

        # Sticky Checkout
        self.checkout = page.locator(
            '[name="checkout"]'
        )

    def open_product(self, product_name):

        product = self.page.locator(
            f'img[alt="{product_name}"]'
        )

        expect(product).to_be_visible()

        product.click()

        # Wait for visible PDP product title
        expect(
            self.product_title
        ).to_be_visible()

    def get_product_name(self):

        expect(
            self.product_title
        ).to_be_visible()

        return self.product_title.inner_text().strip()

    def is_product_available(self):

        return self.add_to_cart.is_enabled()

    def add_product_to_cart(self):

        expect(
            self.add_to_cart
        ).to_be_visible()

        expect(
            self.add_to_cart
        ).to_be_enabled()

        self.add_to_cart.scroll_into_view_if_needed()

        self.add_to_cart.click()

    def click_sticky_checkout(self):

        expect(
            self.checkout
        ).to_be_visible()

        expect(
            self.checkout
        ).to_be_enabled()

        self.checkout.click()