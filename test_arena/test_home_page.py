import re
from playwright.sync_api import expect

from fixtures import home_page
from test_data.pages.header_data import HEADER_DATA
from test_data.pages.home_page_data import HOME_PAGE
from test_data.pages.side_menu_data import SIDE_MENU_DATA


def test_has_title(home_page):
    home_page.open()

    expect(home_page.page).to_have_url(re.compile(HOME_PAGE.end_point))
    expect(home_page.page).to_have_title(HOME_PAGE.title)
    expect(home_page.main_header).to_have_text(HOME_PAGE.main_header)

    expect(home_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)
    expect(home_page.header.logo).to_have_text(HEADER_DATA.logo_text)