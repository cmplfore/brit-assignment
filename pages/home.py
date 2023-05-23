from playwright.sync_api import Page


class HomePage:
    HOMEPAGE_URL = "https://www.britinsurance.com"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.cookies_accept = page.get_by_role("link", name="Allow selection")
        self.search_button = page.get_by_role("navigation").get_by_role("button")
        self.search_input = page.get_by_placeholder("Search for people, services or...")
        self.menu_button = page.locator('xpath=//*[contains(@class, "component--header__burger")]')
        self.contact_link = page.get_by_role("link", name="contact")

    def accept_cookies(self) -> None:
        self.cookies_accept.click()

    def load(self) -> None:
        self.page.goto(self.HOMEPAGE_URL, wait_until='networkidle')

    def search(self, phrase: str) -> None:
        self.search_button.click()
        self.search_input.click()
        self.search_input.fill(phrase)
        self.search_button.click()

    def open_menu(self) -> None:
        self.menu_button.click()

    def open_contact_page(self) -> None:
        self.contact_link.click()
