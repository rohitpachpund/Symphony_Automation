import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        yield page

        browser.close()


def pytest_addoption(parser):
    parser.addoption(
        "--product",
        action="store",
        default=None,
        help="Product to test"
    )

@pytest.fixture
def product_name(request):
    product = request.config.getoption("--product")

    if not product:
        product = "Silenzo"

    return product

