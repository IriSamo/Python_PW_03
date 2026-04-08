import re
from playwright.sync_api import expect

from fixtures import *
from test_data.pages.accordion_page_data import ACCORDION_PAGE
from test_data.pages.header_data import HEADER_DATA
from test_data.pages.side_menu_data import SIDE_MENU_DATA


def test_has_title_direct_navigation(accordion_page):
	accordion_page.open()

	expect(accordion_page.page).to_have_url(re.compile(ACCORDION_PAGE.end_point))
	expect(accordion_page.page).to_have_title(ACCORDION_PAGE.title)
	expect(accordion_page.main_header).to_have_text(ACCORDION_PAGE.main_header)

	expect(accordion_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)
	expect(accordion_page.header.logo).to_have_text(HEADER_DATA.logo_text)

def test_has_title_navigation_by_side_menu(home_page):
	accordion_page = (
		home_page.open()
		.side_menu
		.clik_accordion()
	)

	expect(accordion_page.page).to_have_url(re.compile(ACCORDION_PAGE.end_point))
	expect(accordion_page.page).to_have_title(ACCORDION_PAGE.title)
	expect(accordion_page.main_header).to_have_text(ACCORDION_PAGE.main_header)

	expect(accordion_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)
	expect(accordion_page.header.logo).to_have_text(HEADER_DATA.logo_text)
