from playwright.sync_api import Locator
from playwright.sync_api import Page
from typing import List


class SearchResultPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.results = page.locator('xpath=//*[contains(@class,"results-container")]//*[contains(@class,"s-results")]/a')
