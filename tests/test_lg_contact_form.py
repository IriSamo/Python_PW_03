from playwright.sync_api import Page, expect

BASE_URL = "https://www.automationtesting.co.uk/"

def open_contact_form(page: Page):
    page.goto(f"{BASE_URL}contactForm.html")


def test_contact_form_verify_elements_visibility(page: Page):
    open_contact_form(page)

    header = page.locator("h2", has_text="Contact Form Test")
    expect(header).to_be_visible()
    expect(page.get_by_placeholder("First Name")).to_be_visible()
    expect(page.get_by_placeholder("Last Name")).to_be_visible()
    expect(page.get_by_placeholder("Email Address")).to_be_visible()
    expect(page.get_by_placeholder("Comments")).to_be_visible()
    expect(page.locator('input[type="reset"]')).to_be_visible()
    expect(page.locator('input[type="submit"]')).to_be_visible()


def test_contact_form_successful_submission(page: Page):
    open_contact_form(page)

    first_name = page.get_by_placeholder("First Name")
    last_name = page.get_by_placeholder("Last Name")
    email = page.get_by_placeholder("Email Address")
    comments = page.get_by_placeholder("Comments")
    submit_button = page.locator('input[type="submit"]')

    first_name.fill("Qa")
    last_name.fill("Tester")
    email.fill("Qa.tester@tests.com")
    comments.fill("This is  test only message.")

    submit_button.click()

    expect(page).to_have_url(f"{BASE_URL}contact-form-thank-you.html")


def test_email_required_with_server_error_message(page: Page):
    open_contact_form(page)

    page.get_by_placeholder("First Name").fill("Qa")
    page.get_by_placeholder("Last Name").fill("Tester")
    page.get_by_placeholder("Comments").fill("Testing required email")

    page.locator('input[type="submit"]').click()

    expect(page).to_have_url(f"{BASE_URL}contact_us.php")
    expect(page.get_by_text("Error: all fields are required")).to_be_visible()


def test_invalid_email_with_server_error_message(page: Page):
    open_contact_form(page)

    page.get_by_placeholder("First Name").fill("Qa")
    page.get_by_placeholder("Last Name").fill("Tester")
    page.get_by_placeholder("Email Address").fill("Qa.tester@")
    page.get_by_placeholder("Comments").fill("Testing invalid email")

    page.locator('input[type="submit"]').click()

    expect(page).to_have_url(f"{BASE_URL}contact_us.php")
    expect(page.get_by_text("Invalid email address")).to_be_visible()

