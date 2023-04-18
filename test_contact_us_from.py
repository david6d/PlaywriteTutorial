
from playwright.sync_api import Playwright
from contact_us_page import ContactUsPage

@pytest.mark.skip(reason="not ready")
def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("David", "123 Main", "david@gmail.com", "444555888", "test subject", "automatic test")


# with sync_playwright() as playwright:
#     test_submit_form(playwright)