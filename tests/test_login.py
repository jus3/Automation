import os
import pytest
from Pages.login_details import LoginPage
from testdata.login import LoginData

def test_user_can_login(page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(LoginData.USERNAME, LoginData.PASSWORD)

    page.get_by_role("heading", name="Enter the 6-digit code from your authenticator app")
    assert page.get_by_role("heading", name="Enter the 6-digit code from your authenticator app").is_visible()