import re

import pytest
from playwright.sync_api import expect

from test_data.pages.contact_form_page_data import CONTACT_FORM_PAGE

from fixtures import contact_form_page
from test_data.contact_form_request import negative_requests_data, positive_requests_data


class TestContactForm:

	def test_contact_form_verify_elements_visibility(self, contact_form_page):
		expect(contact_form_page.main_header).to_be_visible()
		expect(contact_form_page.first_name_input).to_be_visible()
		expect(contact_form_page.last_name_input).to_be_visible()
		expect(contact_form_page.email_input).to_be_visible()
		expect(contact_form_page.comments_input).to_be_visible()
		expect(contact_form_page.reset_button).to_be_visible()
		expect(contact_form_page.submit_button).to_be_visible()

	def test_contact_form_successful_submission(self, contact_form_page):
		contact_form_page.fill_contact_form(
			first_name=CONTACT_FORM_PAGE.valid_first_name,
			last_name=CONTACT_FORM_PAGE.valid_last_name,
			email=CONTACT_FORM_PAGE.valid_email,
			comments=CONTACT_FORM_PAGE.valid_comments,
		)
		contact_form_page.click_submit()

		expect(contact_form_page.page).to_have_url(
			contact_form_page.BASE_URL + CONTACT_FORM_PAGE.thank_you_end_point
		)

	def test_contact_form_email_required_with_server_error_message(self, contact_form_page):
		contact_form_page.fill_contact_form(
			first_name=CONTACT_FORM_PAGE.valid_first_name,
			last_name=CONTACT_FORM_PAGE.valid_last_name,
			comments=CONTACT_FORM_PAGE.required_email_comments,
		)
		contact_form_page.click_submit()

		expect(contact_form_page.page).to_have_url(
			contact_form_page.BASE_URL + CONTACT_FORM_PAGE.error_end_point
		)
		expect(contact_form_page.page.get_by_text(CONTACT_FORM_PAGE.all_fields_required_error)).to_be_visible()

	def test_contact_form_invalid_email_with_server_error_message(self, contact_form_page):
		contact_form_page.fill_contact_form(
			first_name=CONTACT_FORM_PAGE.valid_first_name,
			last_name=CONTACT_FORM_PAGE.valid_last_name,
			email=CONTACT_FORM_PAGE.invalid_email,
			comments=CONTACT_FORM_PAGE.invalid_email_comments,
		)
		contact_form_page.click_submit()

		expect(contact_form_page.page).to_have_url(
			contact_form_page.BASE_URL + CONTACT_FORM_PAGE.error_end_point
		)
		expect(contact_form_page.page.get_by_text(CONTACT_FORM_PAGE.invalid_email_error)).to_be_visible()

	@pytest.mark.parametrize("first_name,last_name,email,message", positive_requests_data)
	def test_positive_contact_form_submission(self, contact_form_page, first_name, last_name, email, message):
		contact_form_page.fill_contact_form(first_name, last_name, email, message)

		expect(contact_form_page.first_name_input).to_have_value(first_name)
		expect(contact_form_page.last_name_input).to_have_value(last_name)
		expect(contact_form_page.email_input).to_have_value(email)
		expect(contact_form_page.comments_input).to_have_value(message)

		contact_form_page.click_submit()

		expect(contact_form_page.page).to_have_url(re.compile(r"/contact-form-thank-you.html"))
		expect(contact_form_page.page.locator("body")).to_contain_text("Thank you for your mail!")

	@pytest.mark.parametrize("first_name,last_name,email,message", negative_requests_data)
	def test_negative_contact_form_submission(self, contact_form_page, first_name, last_name, email, message):
		contact_form_page.fill_contact_form(first_name, last_name, email, message)

		contact_form_page.click_submit()

		expect(contact_form_page.page).to_have_url(re.compile(r"/contact_us.php"))
		expect(contact_form_page.page.locator("body")).to_contain_text("Error")
