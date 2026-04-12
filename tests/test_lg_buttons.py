from playwright.sync_api import Page, expect


def test_button_one_click(page: Page):

    page.goto("https://www.automationtesting.co.uk/buttons.html")

   # button_one = page.locator("//button[normalize-space()='BUTTON ONE']")
    #button_one = page.locator('#btn_one')
    button_one = page.get_by_role("button", name="BUTTON ONE")
    expect(button_one).to_be_visible()

    dialog_messages = []

    def handle_dialog(dialog):
        dialog_messages.append(dialog.message)
        dialog.accept()

    page.on("dialog", handle_dialog)

    button_one.click()

    assert dialog_messages[0] == "You clicked the first button!"

    expect(button_one).to_be_enabled()


def test_button_four_disabled(page: Page):
    page.goto("https://www.automationtesting.co.uk/buttons.html")

    button_four = page.get_by_role("button", name="BUTTON FOUR")

    expect(button_four).to_be_visible()
    expect(button_four).to_be_disabled()

   # page.on("dialog", lambda dialog: pytest.fail(f"Dialog appeared for
    # disabled button: {dialog.message}"))


    button_four.click(force=True)
