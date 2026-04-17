import pytest
from playwright.sync_api import expect

from pom_arena.contact_form_page import ContactFormPage
from test_data.pages.contact_form_page_data import CONTACT_FORM_PAGE

@pytest.fixture
def contact_form_page(page):
    return ContactFormPage(page).open()


def test_contact_form_verify_elements_visibility(contact_form_page):
   expect(contact_form_page.main_header).to_be_visible()
   expect(contact_form_page.first_name_input).to_be_visible()
   expect(contact_form_page.last_name_input).to_be_visible()
   expect(contact_form_page.email_input).to_be_visible()
   expect(contact_form_page.comments_input).to_be_visible()
   expect(contact_form_page.reset_button).to_be_visible()
   expect(contact_form_page.submit_button).to_be_visible()


def test_contact_form_successful_submission(contact_form_page):

    contact_form_page.fill_contact_form(
        first_name="Qa",
        last_name="Tester",
        email="qa.tester@tests.com",
        comments="This is test only message."
    )
    contact_form_page.click_submit()

    expect(contact_form_page.page).to_have_url(
        contact_form_page.BASE_URL + CONTACT_FORM_PAGE.thank_you_end_point
    )

def test_contact_form_email_required_with_server_error_message(contact_form_page):
    contact_form_page.fill_contact_form(
        first_name="Qa",
        last_name="Tester",
        comments="Testing required email"
    )
    contact_form_page.click_submit()

    expect(contact_form_page.page).to_have_url(
        contact_form_page.BASE_URL + CONTACT_FORM_PAGE.error_end_point
    )
    expect(contact_form_page.page.get_by_text(CONTACT_FORM_PAGE.all_fields_required_error)).to_be_visible()


def test_contact_form_invalid_email_with_server_error_message(contact_form_page):

    contact_form_page.fill_contact_form(
        first_name="Qa",
        last_name="Tester",
        email="qa.tester@",
        comments="Testing invalid email"
    )
    contact_form_page.click_submit()

    expect(contact_form_page.page).to_have_url(
        contact_form_page.BASE_URL + CONTACT_FORM_PAGE.error_end_point
    )
    expect(contact_form_page.page.get_by_text(CONTACT_FORM_PAGE.invalid_email_error)).to_be_visible()