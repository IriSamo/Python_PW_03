from playwright.sync_api import expect

from fixtures import home_page
from test_data.pages.side_menu_data import SIDE_MENU_DATA


def test_sidebar_menu_all(home_page):
    home_page.open()

    expect(home_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)

    for label in SIDE_MENU_DATA.labels:
        link = home_page.side_menu.get_menu_link(label)
        expect(link).to_be_visible()