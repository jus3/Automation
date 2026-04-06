from playwright.sync_api import expect

from Pages.signin_details import SigninPage
from testdata.Signin import SigninData

def test_user_can_signin(page):

    login_page = SigninPage(page)
    login_page.login(SigninData.email, SigninData.PASSWORD)

#   assert page.get_by_role("heading", name="My account")
    expect(page.get_by_role("heading", name="My account")).to_be_visible()

