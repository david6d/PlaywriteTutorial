from playwright.sync_api import Playwright, sync_playwright, expect
from Home_page_elements import HomePage
import pytest

@pytest.mark.integration
def test_about_us_section_variable(login_set_up):
    page = login_set_up
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    print("aha")

#@pytest.mark.skip(reason="not ready")
#@pytest.mark.xfail(reason=" url not ready")
@pytest.mark.regression
def test_about_us_section_variable_2(login_set_up):
    page = login_set_up
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    print("aha")
