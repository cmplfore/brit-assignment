import pytest

from pages.home import HomePage
from pages.search import SearchResultPage
from pages.contact import ContactPage
from playwright.sync_api import Page


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def results_page(page: Page) -> SearchResultPage:
    return SearchResultPage(page)


@pytest.fixture
def contact_page(page: Page) -> ContactPage:
    return ContactPage(page)
