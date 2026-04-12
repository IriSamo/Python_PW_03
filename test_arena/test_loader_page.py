import re
from playwright.sync_api import expect

from fixtures import *
from test_data.pages.loader_page_data import LOADER_PAGE
from test_data.pages.header_data import HEADER_DATA
from test_data.pages.side_menu_data import SIDE_MENU_DATA


def test_has_title_direct_navigation(loader_page):
	loader_page.open()

	expect(loader_page.page).to_have_url(re.compile(LOADER_PAGE.end_point))
	expect(loader_page.page).to_have_title(LOADER_PAGE.title)
	expect(loader_page.main_header).to_have_text(LOADER_PAGE.main_header)

	expect(loader_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)
	expect(loader_page.header.logo).to_have_text(HEADER_DATA.logo_text)

def test_loader_completed(loader_page):
	loader_page.open()

	expect(loader_page.loader).to_be_visible()
	expect(loader_page.loader).to_be_hidden(timeout=7_000)
	expect(loader_page.loading_complete_message).to_be_visible()
