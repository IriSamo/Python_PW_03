import re
from playwright.sync_api import expect

from fixtures import *
from test_data.pages.browser_tab_page_data import BROWSER_TAB_PAGE
from test_data.pages.header_data import HEADER_DATA
from test_data.pages.side_menu_data import SIDE_MENU_DATA


def test_has_title_direct_navigation(browser_tab_page):
    browser_tab_page.open()

    expect(browser_tab_page.page).to_have_url(re.compile(BROWSER_TAB_PAGE.end_point))
    expect(browser_tab_page.page).to_have_title(BROWSER_TAB_PAGE.title)
    expect(browser_tab_page.main_header).to_have_text(BROWSER_TAB_PAGE.main_header)

    expect(browser_tab_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)
    expect(browser_tab_page.header.logo).to_have_text(HEADER_DATA.logo_text)

def test_open_new_browser_page_1(page, browser_tab_page, context):
    # page.pause()
    browser_tab_page.open()

    new_page = None

    def handle_page(page):
        nonlocal new_page
        page.wait_for_load_state()
        new_page = page

    context.on("page", handle_page)

    browser_tab_page.click_open_tab_btn()

    expect(new_page).to_have_url(re.compile(r"google.com.*"))


def test_open_new_browser_page_2(browser_tab_page, context):
    browser_tab_page.open()

    with context.expect_event("page") as event_info:
        browser_tab_page.click_open_tab_btn()

    new_page = event_info.value
    new_page.wait_for_load_state()

    expect(new_page).to_have_url(re.compile(r"google.com.*"))


def test_open_new_browser_page_3(browser_tab_page):
    browser_tab_page.open()

    with browser_tab_page.page.expect_popup() as popup_info:
        browser_tab_page.click_open_tab_btn()

    new_page = popup_info.value
    new_page.wait_for_load_state()

    expect(new_page).to_have_url(re.compile(r"google.com.*"))
