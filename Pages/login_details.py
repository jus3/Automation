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
        # 1. Click the 'Log In' button to open the form
        self.login_button.click()

        # 2. Fill the inputs using the arguments passed to this function
        self.username_input.fill(username)
        self.password_input.fill(password)

        # 3. Submit the form
        self.submit_button.click()