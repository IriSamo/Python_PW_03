from playwright.sync_api import Page, expect

def test_slidebar_menu_all(page : Page):
    page.goto("https://www.automationtesting.co.uk/")

    LABELS_EXPECTED  = [

        "Homepage",
        "Accordion",
        "Actions",
        "Browser Tabs",
        "Buttons",
        "Calculator (JS)",
        "Contact Us Form Test",
        "Date Picker",
        "DropDown Checkbox Radio",
        "File Upload",
        "Hidden Elements",
        "iFrames",
        "Loader",
        "Loader Two",
        "Login Portal Test",
        "Mouse Movement",
        "Pop Ups & Alerts",
        "Predictive Search",
        "Tables",
        "Test Store",
        "About Me",
    ]

    header = page.locator("h2", has_text ='Menu')
    expect(header).to_be_visible()

    for label in LABELS_EXPECTED:
        link = page.locator("ul li a").filter(has_text=label).first
        #link = page.get_by_role("link", name=label, exact=True)
        expect(link).to_be_visible()
        print(f" '{label}' is visible")







