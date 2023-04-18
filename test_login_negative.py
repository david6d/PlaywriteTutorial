# import time
# from playwright.sync_api import Playwright,expect
# import pytest
#
#
#
# @pytest.mark.parametrize("email", ["pemake5422@mustbeit.com",
#                                             pytest.param("fakeemail", marks=pytest.mark.xfail),
#                                             pytest.param("pemake5422@mustbeit", marks=pytest.mark.xfail)])
# @pytest.mark.parametrize("password", ["simson",
#                                             pytest.param("fakepassword", marks=pytest.mark.xfail),
#                                             "simson"])
# def test_user_can_login(page, email, password) -> None:
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     page.wait_for_load_state("networkidle")
#     login_issue = True
#     while login_issue:
#         if not page.is_visible("data-testid=signUp.switchToSignUp"):
#             page.locator("button:has-text(\"Log In\")").click()
#         else:
#             login_issue = False
#         time.sleep(0.5)
#
#     page.get_by_test_id("signUp.switchToSignUp").click()
#     page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
#     page.locator(":nth-match(input[type=email], 2)").fill(email)
#     page.get_by_label("Password").fill(password, timeout=2000)
#     page.get_by_label("Password").press("Enter")
#     page.wait_for_timeout(3000)
#     expect(page.get_by_role("button", name="Log In")).to_be_hidden(timeout=2000)
#     page.close()
#     print("aha")