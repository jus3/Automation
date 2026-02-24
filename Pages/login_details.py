from playwright.sync_api import Page
from testdata.login import LoginData

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.login_button = page.get_by_role("link", name="Log In")
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.submit_button = page.get_by_role("button", name="Log In")

    def navigate(self):
        self.page.goto("https://www.reddit.com/")

    def login(self, username, password):

        self.login_button.click()

        self.username_input.fill(username)
        self.password_input.fill(password)

        self.submit_button.click()