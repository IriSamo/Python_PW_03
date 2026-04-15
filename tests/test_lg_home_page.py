from playwright.sync_api import Page, expect

URL = "https://www.automationtesting.co.uk/"

def test_homepage_h1_header(page : Page):
    page.goto(URL)
    header1 = page.locator("h1" , has_text="Testing Arena")
    expect(header1).to_be_visible()

def test_homepage_url(page: Page):
    page.goto(URL)
    expect (page).to_have_url(URL)

def test_homepage_title(page: Page):
    page.goto(URL)
    expect(page).to_have_title("Homepage")

def test_homepage_logo(page : Page):
    page.goto(URL)
    logo = page.locator(".logo")
    expect(logo).to_be_visible()

def test_homepage_hamburger_opens_sidebar_menu(page: Page):
    page.goto(URL)
    sidebar = page.locator("#sidebar")

    hamburger = page.locator("a.toggle")
    hamburger.click()

    expect(sidebar).not_to_have_class("inactive")
