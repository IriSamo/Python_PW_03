from dataclasses import dataclass


@dataclass(frozen=True)
class ContactFormPageData:
    thank_you_end_point: str
    error_end_point: str
    all_fields_required_error: str
    invalid_email_error: str
    valid_first_name: str
    valid_last_name: str
    valid_email: str
    valid_comments: str
    invalid_email: str
    required_email_comments: str
    invalid_email_comments: str


CONTACT_FORM_PAGE = ContactFormPageData(
    thank_you_end_point="/contact-form-thank-you.html",
    error_end_point="/contact_us.php",
    all_fields_required_error="Error: all fields are required",
    invalid_email_error="Invalid email address",
    valid_first_name="Qa",
    valid_last_name="Tester",
    valid_email="qa.tester@tests.com",
    valid_comments="This is test only message.",
    invalid_email="qa.tester@",
    required_email_comments="Testing required email",
    invalid_email_comments="Testing invalid email",
)