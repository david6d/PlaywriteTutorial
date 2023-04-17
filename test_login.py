import time
from playwright.sync_api import Playwright,expect
import pytest


@pytest.mark.smoke
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:
    page = login_set_up
    #page.get_by_role("button", name="Log In").click()    1  default
    #page.get_by_role("link", name="Contact Us").click()  2  default
    #page.locator("p[id=comp-kqx7ocfp4label]").click()    3  selectors
    #page.locator("button:has-text('Contact Us')").click() 4 does not work may be on this page
    #page.wait_for_timeout(15000)
    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("data-testid=signUp.switchToSignUp"):
    #         page.locator("button:has-text(\"Log In\")").click()
    #     else:
    #         login_issue = False
    #


    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden(timeout=7000)
    print("aha")






