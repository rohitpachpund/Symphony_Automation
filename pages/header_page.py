from playwright.sync_api import Page


class HeaderPage:

    def __init__(self, page: Page):
        self.page = page

        # =========================
        # Header
        # =========================

        self.logo = page.locator(
            "div[class='hamburger-logo-main'] a"
        )

        self.all_category = page.locator(
            'a:has-text("All Category")'
        )

        # =========================
        # Air Coolers
        # =========================

        self.air_coolers = page.locator(
            "#myDropdown"
        )

        self.cooler = page.locator(
            "//div[@class='has-submenu']//a[normalize-space()='Air Coolers']"
        )

        self.all_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(0)

        self.premium_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(1)

        self.silent_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(2)

        self.desert_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(3)

        self.tower_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(4)

        self.industrial_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(5)

        self.bedroom_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(6)

        self.living_room_cooler = page.locator(
            "div.submenu"
        ).locator("a").nth(7)

        # =========================
        # Geyser
        # =========================

        self.geysers = page.locator(
            "//div[@id='myDropdown']//a[normalize-space()='Hairfall Control Geysers']"
        )

        # =========================
        # Tower & Kitchen Fans
        # =========================

        self.tower_kitchen = page.locator(
            "//div[@class='has-submenu']//a[normalize-space()='Tower & Kitchen Cooling Fans']"
        )

        self.tower_fans = page.locator("//div[@class='submenu']//a[normalize-space()='Tower Fans']")

        self.kitchen_fans = page.locator("//div[@class='submenu']//a[contains(text(),'Kitchen Cooling Fan')]")
        # =========================
        # Search
        # =========================

        self.search_bar = page.locator(
            "#desktop-search-input"
        )

        self.search_result_title = page.locator(
            "h1.sec-title"
        )

        # =========================
        # Header Redirections
        # =========================

        self.tracking = page.locator(
            "//img[@alt='Location Icon']"
        )

        self.support = page.locator(
            "//a[@href='https://shop.symphonylimited.com/pages/contactus']//img[@alt='Support Icon']"
        )

        self.account = page.locator("//img[@alt='Account Icon']")
        self.account_popup_title = page.locator("div#login-wrapper p.header-text")

        # PINCODE
        # PINCODE

     # PINCODE

        self.pincode_trigger = page.get_by_text(
    "Update Delivery Pincode",
    exact=True
).first

        self.pincode = page.locator(
    "//div[@class='pincode-checker']//div[@class='pc-wrapper']//input"
)

        self.pincode_enter = page.locator(
    ".pincode-input-field"
)

        self.update_pincode = page.locator(
    ".pincode-submit-btn"
)

        self.delivery_message = page.locator(
    "p.express-delivery-text"
)

        self.invalid_pincode_message = page.locator(
    ".pincode-error-message"
)


    # ==================================================
    # HEADER
    # ==================================================

    def open_all_category(self):
        self.all_category.click()

    # ==================================================
    # AIR COOLERS
    # ==================================================

    def air_cooler_opened(self):
        self.cooler.hover()

    def all_cooler_opened(self):
        self.all_cooler.click()

    def premium_cooler_opened(self):
        self.premium_cooler.click()

    def silent_cooler_opened(self):
        self.silent_cooler.click()

    def desert_cooler_opened(self):
        self.desert_cooler.click()

    def tower_cooler_opened(self):
        self.tower_cooler.click()

    def industrial_cooler_opened(self):
        self.industrial_cooler.click()

    def bedroom_cooler_opened(self):
        self.bedroom_cooler.click()

    def living_room_cooler_opened(self):
        self.living_room_cooler.click()

    # ==================================================
    # GEYSER
    # ==================================================

    def geyser_opened(self):
        self.geysers.click()

    # ==================================================
    # FANS
    # ==================================================

    def tower_kitchen_opened(self):
        self.tower_kitchen.hover()

    def tower_fans_opened(self):
        self.tower_fans.click()

    def kitchen_cooling_fans_opened(self):
        self.kitchen_fans.click()

    # ==================================================
    # SEARCH
    # ==================================================

    def search_product(self, product_name):
        self.search_bar.fill(product_name)
        self.search_bar.press("Enter")

    # ==================================================
    # HEADER REDIRECTIONS
    # ==================================================

    def tracking_opened(self):
     with self.page.expect_popup() as popup_info:
        self.tracking.click()

     return popup_info.value
    
    def account_opened(self):
     self.account.click()


    def enter_pincode(self, pincode):
     self.pincode_trigger.click()
     self.pincode_enter.fill(pincode)
     self.update_pincode.click()