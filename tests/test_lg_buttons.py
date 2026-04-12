from playwright.sync_api import Page, expect


def test_button_one_click(page: Page):

    page.goto("https://www.automationtesting.co.uk/buttons.html")

   # button_one = page.locator("//button[normalize-space()='BUTTON ONE']")
    #button_one = page.locator('#btn_one')
    button_one = page.get_by_role("button", name="BUTTON ONE")
    expect(button_one).to_be_visible()

    with page.expect_event("dialog") as dialog_info:
        button_one.click()

    dialog = dialog_info.value
    print(f"Pop-up message: {dialog.message}")
    assert dialog.message == "You clicked the first button!"
    dialog.accept()
    page.wait_for_timeout(3000)
    expect(button_one).to_be_enabled()

def test_button_four_disabled(page: Page):
    page.goto("https://www.automationtesting.co.uk/buttons.html")

    button_four = page.get_by_role("button", name="BUTTON FOUR")

    expect(button_four).to_be_visible()
    expect(button_four).to_be_disabled()

   # page.on("dialog", lambda dialog: pytest.fail(f"Dialog appeared for
    # disabled button: {dialog.message}"))


    button_four.click(force=True)
