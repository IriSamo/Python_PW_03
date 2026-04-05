import re
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def before_each(page):
    page.goto("https://www.automationtesting.co.uk/actions.html")

def test_actions_title(page: Page):
    expect(page).to_have_title(re.compile("Actions"))

def test_drag_and_drop(page: Page):
    drag_element = page.get_by_text("Drag me!")
    drop_target = page.locator(".droptarget").nth(1)

    drag_element.drag_to(drop_target)

    demo_text = page.locator("#demo").inner_text()
    assert demo_text == "The p element was dropped into an accepted rectangle"

def test_click_and_hold(page: Page):
    click_box = page.locator("#click-box")

    click_box.hover()
    page.mouse.down()

    assert click_box.inner_text() == "Keep holding down!"
    assert click_box.evaluate("el => el.style.background") in ("rgb(199, 255, 188)", "#c7ffbc")

    page.mouse.up()

    assert click_box.inner_text() == "No, don't let go :("
    assert click_box.evaluate("el => el.style.background") in ("rgb(255, 188, 188)", "#ffbcbc")

def test_double_click(page: Page):
    double_click_area = page.locator("#doubleClickArea").first

    expect(double_click_area).to_contain_text("Double Click Here")
    double_click_area.dblclick()

    assert page.locator("#doubClickStartText").first.inner_text() == "Well Done!"
    assert double_click_area.evaluate("el => el.style.backgroundColor") == "rgb(199, 255, 188)"

def test_shift_click(page: Page):
    click_area = page.locator("#doubleClickArea").nth(1)
    message = None

    def handle_dialog(dialog):
        nonlocal message
        message = dialog.message
        dialog.accept()

    page.once("dialog", handle_dialog)
    click_area.click()
    assert "The SHIFT key was NOT pressed!" in message

    page.once("dialog", handle_dialog)
    click_area.click(modifiers=["Shift"])
    assert "The SHIFT key was pressed!" in message