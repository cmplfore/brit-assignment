from playwright.sync_api import Page


class ContactPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.bermuda_address = page.locator('xpath=//*[@id="bermudaoffice"]//address')

    def format_bermuda_address(self) -> str:
        formatted_address = self.bermuda_address.inner_text().strip().replace('\n', ' ')
        return formatted_address
