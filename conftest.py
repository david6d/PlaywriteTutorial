import os
import pytest
import time
#from playwright.sync_api import Playwright



try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture(scope="session")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    yield page


@pytest.fixture(scope="session")
def login_set_up(set_up):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page = set_up
    login_issue = True
    while login_issue:
        if not page.is_visible("data-testid=signUp.switchToSignUp"):
            page.locator("button:has-text(\"Log In\")").click()
        else:
            login_issue = False
        time.sleep(0.5)

    # page.locator("text=Log In").click()

    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").fill("pemake5422@mustbeit.com")
    # page.locator("input:below(:text('Email'))").fill("pemake5422@mustbeit.com") CSS does not work may be on this page
    page.locator(":nth-match(input[type=email], 2)").fill("pemake5422@mustbeit.com")  # selectors
    # page.get_by_test_id("emailAuth").get_by_label("Email").press("Enter")
    page.get_by_label("Password").fill(PASSWORD, timeout=2000)
    page.get_by_label("Password").press("Enter")

    yield page
