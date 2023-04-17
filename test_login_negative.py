import time
from playwright.sync_api import Playwright,expect
import pytest



@pytest.mark.parametrize("email", ["pemake5422@mustbeit.com",
                                            pytest.param("fakeemail", marks=pytest.mark.xfail),
                                            pytest.param("pemake5422@mustbeit", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["simson",
                                            pytest.param("fakepassword", marks=pytest.mark.xfail),
                                            "simson"])
def test_user_can_login(page, email, password) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
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
    page.locator(":nth-match(input[type=email], 2)").fill(email)  # selectors
    # page.get_by_test_id("emailAuth").get_by_label("Email").press("Enter")
    page.get_by_label("Password").fill(password, timeout=2000)
    page.get_by_label("Password").press("Enter")
    #page.wait_for_load_state("networkidle")
    page.wait_for_timeout(3000)
    expect(page.get_by_role("button", name="Log In")).to_be_hidden(timeout=2000)
    page.close()
    print("aha")