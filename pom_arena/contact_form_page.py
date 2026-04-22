from functools import cached_property
from pom_arena.base_page import BasePage


class ContactFormPage(BasePage):
    END_POINT = "/contactForm.html"

    def __init__(self, page):
        super().__init__(page, self.END_POINT)

    @cached_property
    def main_header(self):
        return self._main_body.locator("h2", has_text="Contact Form Test")

    @cached_property
    def first_name_input(self):
        return self._main_body.get_by_placeholder("First Name")

    @cached_property
    def last_name_input(self):
        return self._main_body.get_by_placeholder("Last Name")

    @cached_property
    def email_input(self):
        return self._main_body.get_by_placeholder("Email Address")

    @cached_property
    def comments_input(self):
        return self._main_body.get_by_placeholder("Comments")

    @cached_property
    def reset_button(self):
        return self._main_body.locator('input[type="reset"]')

    @cached_property
    def submit_button(self):
        return self._main_body.locator('input[type="submit"]')

    def fill_first_name(self, first_name):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name):
        self.last_name_input.fill(last_name)

    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_comments(self, comments):
        self.comments_input.fill(comments)

    def fill_contact_form(self, first_name="", last_name="", email="", comments=""):
        if first_name:
            self.fill_first_name(first_name)
        if last_name:
            self.fill_last_name(last_name)
        if email:
            self.fill_email(email)
        if comments:
            self.fill_comments(comments)

    def click_submit(self):
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")

    def click_reset(self):
        self.reset_button.click()