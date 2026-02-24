from Pages.login_details import LoginPage
from testdata.login import LoginData
from playwright.sync_api import Page

def test_user_can_login(page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(LoginData.USERNAME, LoginData.PASSWORD)

    assert page.get_by_role("heading", name="Enter the 6-digit code from your authenticator app")