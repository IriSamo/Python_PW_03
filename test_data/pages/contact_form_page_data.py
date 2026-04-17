from dataclasses import dataclass


@dataclass(frozen=True)
class ContactFormPageData:
    end_point: str
    thank_you_end_point: str
    error_end_point: str
    main_header: str
    all_fields_required_error: str
    invalid_email_error: str


CONTACT_FORM_PAGE = ContactFormPageData(
	end_point="/contactForm.html",
    main_header="Contact Form Test",
	thank_you_end_point="/contact-form-thank-you.html",
	error_end_point="/contact_us.php",
	all_fields_required_error="Error: all fields are required",
    invalid_email_error="Invalid email address",
)