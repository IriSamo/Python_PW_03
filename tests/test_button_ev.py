import re
import time
from playwright.sync_api import Page, expect


def test_button_list_visible(page):
    page.goto('https://www.automationtesting.co.uk/index.html')

    page.locator("a[href='buttons.html']").click()

    #checking the WebElement.click()
    label1 = page.locator("h3:has-text('WebElement.click()')")
    assert label1.is_visible()

    button1 = page.locator("#btn_one")
    button1.click()


    #checking JavaScript click
    label2 = page.locator("h3:has-text('JavaScript click')")
    assert label2.is_visible()

    button2 = page.locator("#btn_two")
    button2.click()


    #checking Action Move & Click
    label3 = page.locator("h3:has-text('Action Move & Click')")
    assert label3.is_visible()

    button3 = page.locator("#btn_three")
    button3.click()

    #checking Disabled Button
    label4 = page.locator("h3:has-text('Disabled Button')")
    assert label4.is_visible()

    button4 = page.locator("#btn_four")
    expect(button4).to_be_disabled()











