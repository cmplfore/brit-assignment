from playwright.sync_api import expect, Page
from pages.home import HomePage
from pages.search import SearchResultPage
from pages.contact import ContactPage


def test_home_page_search(page: Page,
                          results_page: SearchResultPage,
                          home_page: HomePage) -> None:
    home_page.load()
    home_page.accept_cookies()

    expect(page).to_have_title('Brit Insurance')

    home_page.search('IFRS 17')
    expect(page).to_have_title('Search')
    expect(results_page.results).to_have_text([
        'Interim results for the six months ended 30 June 2022',
        'Gavin Wilkinson',
        'John King'])


def test_home_page_contact_us_navigation(page: Page,
                                         contact_page: ContactPage,
                                         home_page: HomePage) -> None:
    home_page.load()
    home_page.accept_cookies()

    expect(page).to_have_title('Brit Insurance')

    home_page.open_menu()
    home_page.open_contact_page()
    expect(page).to_have_title('Contact')

    assert 'Ground Floor, Chesney House The Waterfront, 96 Pitts Bay Road, Pembroke, Hamilton HM 08, Bermuda' in contact_page.format_bermuda_address()
