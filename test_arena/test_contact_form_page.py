import re

import pytest
from playwright.sync_api import expect

from fixtures import contact_form_page
from test_data.contact_form_request import negative_requests_data, positive_requests_data


class TestContactForm:
	@pytest.mark.parametrize("first_name,last_name,email,message", positive_requests_data)
	def test_positive_contact_form_submission(self, contact_form_page, first_name, last_name, email, message):
		"""Test that valid contact form submissions are accepted."""
		contact_form_page.open()
		contact_form_page.fill_form(first_name, last_name, email, message)
		
		# Verify fields are filled correctly before submission
		expect(contact_form_page.first_name_field).to_have_value(first_name)
		expect(contact_form_page.last_name_field).to_have_value(last_name)
		expect(contact_form_page.email_field).to_have_value(email)
		expect(contact_form_page.message_field).to_have_value(message)
		
		# Submit the form
		contact_form_page.submit_form()

		expect(contact_form_page.page).to_have_url(re.compile(r"/contact-form-thank-you.html"))
		expect(contact_form_page.page.locator("body")).to_contain_text("Thank you for your mail!")

	@pytest.mark.parametrize("first_name,last_name,email,message", negative_requests_data)
	def test_negative_contact_form_submission(self, contact_form_page, first_name, last_name, email, message):
		"""Test that invalid contact form submissions are handled."""
		contact_form_page.open()
		contact_form_page.fill_form(first_name, last_name, email, message)
		
		# Submit the form
		contact_form_page.submit_form()

		expect(contact_form_page.page).to_have_url(re.compile(r"/contact_us.php"))
		expect(contact_form_page.page.locator("body")).to_contain_text("Error")