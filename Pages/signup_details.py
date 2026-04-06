from playwright.sync_api import Page

class SignupDetails:
    def __init__(self, page: Page):
        self.page = page

        self.signup_button = page.get_by_role("link", name="Sign up")
        self.username_inout= page.get_by_role("textbox", name="Username:")
        self.password_input= page.get_by_role("textbox", name="Password:")
        self.confirm_signup_button = page.get_by_role("button", name="Sign up")

    def signup(self, username, password):
        self.signup_button.click()

        self.username_inout.fill(username)
        self.password_input.fill(password)

        self.confirm_signup_button.click()