from playwright.sync_api import expect, Page


def test_home_page_search(page: Page) -> None:
    page.goto('https://www.britinsurance.com', wait_until='networkidle')
    expect(page).to_have_title('Brit Insurance')
    page.get_by_role("link", name="Allow selection").click()
    page.get_by_role("navigation").get_by_role("button").click()
    page.get_by_placeholder("Search for people, services or...").click()
    page.get_by_placeholder("Search for people, services or...").fill("IFRS 17")
    expect(page.get_by_placeholder("Search for people, services or...")).to_have_value("IFRS 17")
    page.get_by_role("navigation").get_by_role("button").click()
    expect(page).to_have_title('Search')

    results = page.locator('xpath=//*[contains(@class,"results-container")]//*[contains(@class,"s-results")]/a')

    assert len(results.all_text_contents()) >= 3

    expect(results).to_have_text([
        'Interim results for the six months ended 30 June 2022',
        'Gavin Wilkinson',
        'John King'])


def test_home_page_contact_us_navigation(page: Page) -> None:
    page.goto('https://www.britinsurance.com', wait_until='networkidle')
    expect(page).to_have_title('Brit Insurance')
    page.get_by_role("link", name="Allow selection").click()
    page.locator('xpath=//*[contains(@class, "component--header__burger")]').click()
    page.get_by_role("link", name="contact").click()
    expect(page).to_have_title('Contact')

    formatted_address = page.locator('xpath=//*[@id="bermudaoffice"]//address').inner_text().strip().replace('\n',' ')
    assert 'Ground Floor, Chesney House The Waterfront, 96 Pitts Bay Road, Pembroke, Hamilton HM 08, Bermuda' \
           in formatted_address