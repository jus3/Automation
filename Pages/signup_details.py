from playwright.sync_api import Page
from tests.conftest import page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page

        self.register_button = page.get_by_role("link", name="Register your account")
        self.first_name = page.get_by_role("textbox", name="First name")
        self.last_name = page.get_by_role("textbox", name="Last name")
        self.dob = page.get_by_role("textbox", name="Date of birth")
        self.street = page.get_by_role("textbox", name="Street")
        self.postal_code = page.get_by_role("textbox", name="Postal code")
        self.city = page.get_by_role("textbox", name="City")
        self.state = page.get_by_role("textbox", name="State")
        self.country_dropdown = page.get_by_role("combobox", name="Country")
        self.phone = page.get_by_role("textbox", name="Phone")
        self.email = page.get_by_role("textbox", name="Email address")
        self.password = page.get_by_role("textbox", name="Password")
        self.register = page.get_by_role("button", name="Register")

    def select_country(self, country_name):
        self.country_dropdown.click()
        self.page.get_by_role("option", name=country_name)

    def signup(self, first_name, last_name, dob, street, postal_code, city, state, country, phone, email, password):

        self.register_button.click()
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.dob.fill(dob)
        self.street.fill(street)
        self.postal_code.fill(postal_code)
        self.city.fill(city)
        self.state.fill(state)
        self.country_dropdown.fill(country)
        self.phone.fill(phone)
        self.email.fill(email)
        self.password.fill(password)
        self.register.click()