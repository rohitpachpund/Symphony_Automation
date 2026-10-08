from pages.header_page import HeaderPage
from playwright.sync_api import expect
import pytest


# ==========================================================
# LOGO
# ==========================================================

def test_symphony_logo_is_visible(page):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    expect(header.logo).to_be_visible()


# ==========================================================
# ALL CATEGORY
# ==========================================================

def test_all_category_open(page):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.open_all_category()

    expect(header.air_coolers).to_be_visible()


# ==========================================================
# AIR COOLER MENU
# ==========================================================

@pytest.mark.parametrize(
    "menu_method, expected_url",
    [
        (
            "all_cooler_opened",
            "https://shop.symphonylimited.com/collections/all-coolers"
        ),
        (
            "premium_cooler_opened",
            "https://shop.symphonylimited.com/collections/premium-air-cooler"
        ),
        (
            "silent_cooler_opened",
            "https://shop.symphonylimited.com/collections/silent-coolers"
        ),
        (
            "desert_cooler_opened",
            "https://shop.symphonylimited.com/collections/desert-air-coolers"
        ),
        (
            "tower_cooler_opened",
            "https://shop.symphonylimited.com/collections/tower-air-coolers"
        ),
        (
            "industrial_cooler_opened",
            "https://shop.symphonylimited.com/collections/industrial-air-coolers"
        ),
        (
            "bedroom_cooler_opened",
            "https://shop.symphonylimited.com/collections/bedroom-1"
        ),
        (
            "living_room_cooler_opened",
            "https://shop.symphonylimited.com/collections/living-room-1"
        ),
    ]
)
def test_air_cooler_menu(
    page,
    menu_method,
    expected_url
):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.open_all_category()

    header.air_cooler_opened()

    getattr(header, menu_method)()

    expect(page).to_have_url(expected_url)


# ==========================================================
# GEYSER
# ==========================================================

def test_geyser_open(page):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.open_all_category()

    header.geyser_opened()

    expect(page).to_have_url(
        "https://shop.symphonylimited.com/collections/geyser"
    )


# ==========================================================
# FANS
# ==========================================================

@pytest.mark.parametrize(
    "menu_method, expected_url",
    [
        (
            "tower_fans_opened",
            "https://shop.symphonylimited.com/collections/tower-fans"
        ),
        (
            "kitchen_cooling_fans_opened",
            "https://shop.symphonylimited.com/products/duet-i-indias-1st-kitchen-cooling-fan"
        ),
    ]
)
def test_fans_menu(
    page,
    menu_method,
    expected_url
):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.open_all_category()

    header.tower_kitchen_opened()

    getattr(header, menu_method)()

    expect(page).to_have_url(expected_url)


# ==========================================================
# VALID SEARCH
# ==========================================================

@pytest.mark.parametrize(
    "product",
    [
        "cooler",
        "fan",
        "geyser",
    ]
)
def test_valid_product_search(page, product):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.search_product(product)

    expect(
        header.search_result_title
    ).to_contain_text(f'"{product}"')


# ==========================================================
# INVALID SEARCH
# ==========================================================

def test_invalid_product_search(page):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.search_product(
        "1232dfgsdhtk4uj6j4m"
    )

    expect(
        header.search_result_title
    ).to_contain_text("No results for")


# ==========================================================
# HEADER REDIRECTIONS
# ==========================================================



@pytest.mark.smoke
def test_tracking_redirection(page):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    tracking_page = header.tracking_opened()

    expect(tracking_page).to_have_url(
        "https://symphonyd2c.clickpost.ai/"
    )


@pytest.mark.smoke
def test_account_popup(page):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    print("Account count:", header.account.count())
    print("Account visible:", header.account.is_visible())

    header.account_opened()

    page.wait_for_timeout(3000)

    print("Popup title count:", header.account_popup_title.count())

    print("Popup title visible:", header.account_popup_title.is_visible())

    print("India text count:", page.get_by_text("India's Number 1 Air Cooler!", exact=True).count())


    # PINCODE TESTS

@pytest.mark.parametrize(
    "pincode",
    [
        "412101",
        "411001",
        "560001",
        "500001"
    ]
)
def test_valid_pincode(page, pincode):

    page.goto("https://shop.symphonylimited.com/")

    header = HeaderPage(page)

    header.enter_pincode(pincode)

    expect(
        header.delivery_message
    ).to_be_visible()


def test_invalid_pincode(page):

     page.goto("https://shop.symphonylimited.com/")

     header = HeaderPage(page)

     header.enter_pincode("000000")

     expect(
        header.invalid_pincode_message
    ).to_be_visible()

     expect(
        header.invalid_pincode_message
    ).to_have_text("Invalid pincode")