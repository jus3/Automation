from pages.signin_details import SigninPage
from testdata.Signin import SigninData

def test_user_can_signin(page):

    login_page = SigninPage(page)
    login_page.login(SigninData.email, SigninData.PASSWORD)


