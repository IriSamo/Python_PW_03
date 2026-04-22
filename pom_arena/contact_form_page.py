from functools import cached_property

from playwright.sync_api import Page

from pom_arena.base_page import BasePage


class ContactFormPage(BasePage):
	END_POINT = "/contactForm.html"

	def __init__(self, page: Page):
		super().__init__(page, self.END_POINT)

	@cached_property
	def first_name_field(self):
		return self._main_body.get_by_placeholder("First Name")

	@cached_property
	def last_name_field(self):
		return self._main_body.get_by_placeholder("Last Name")

	@cached_property
	def email_field(self):
		return self._main_body.get_by_placeholder("Email Address")

	@cached_property
	def message_field(self):
		return self._main_body.get_by_placeholder("Comments")

	@cached_property
	def submit_button(self):
		return self._main_body.locator('input[type="submit"]')

	def fill_form(self, first_name: str, last_name: str, email: str, message: str):
		self.first_name_field.fill(first_name)
		self.last_name_field.fill(last_name)
		self.email_field.fill(email)
		self.message_field.fill(message)

	def submit_form(self):
		self.submit_button.click()
