from playwright.sync_api import Page, expect

def test_slidebar_menu_all(page : Page):
    page.goto("https://www.automationtesting.co.uk/")
    header1 = page.locator("h1" , has_text="Testing Arena")

    expect(header1).to_be_visible()

    print("'Testing Arena' header is visible")