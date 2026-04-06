from playwright.sync_api import Page
from testdata.Signin import SigninData

class SigninPage:
    def __init__(self, page: Page):
        self.page = page

        self.signin_button = page.get_by_role("link", name="Sign in")
        self.email_input = page.get_by_role("textbox", name="Email address *")
        self.password_input = page.get_by_role("textbox", name="Password *")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, email, password):

        self.signin_button.click()

        self.email_input.fill(email)
        self.password_input.fill(password)

        self.login_button.click()