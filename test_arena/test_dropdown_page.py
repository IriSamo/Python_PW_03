import re
from playwright.sync_api import expect

from fixtures import *
from test_data.pages.dropdown_page_data import DROPDOWN_PAGE
from test_data.pages.header_data import HEADER_DATA
from test_data.pages.side_menu_data import SIDE_MENU_DATA


def test_has_title_direct_navigation(dropdown_page):
	dropdown_page.open()

	expect(dropdown_page.page).to_have_url(re.compile(DROPDOWN_PAGE.end_point))
	expect(dropdown_page.page).to_have_title(DROPDOWN_PAGE.title)
	expect(dropdown_page.main_header).to_have_text(DROPDOWN_PAGE.main_header)

	expect(dropdown_page.side_menu.main_header).to_contain_text(SIDE_MENU_DATA.header)
	expect(dropdown_page.header.logo).to_have_text(HEADER_DATA.logo_text)

def test_dropdown_menu(dropdown_page):
	dropdown_page.open()
	dropdown_page.click_dropdown_menu()

	expect(dropdown_page.dropdown_menu_item).to_have_count(len(DROPDOWN_PAGE.dropdown_menu_dict))
	expected_items_list = list(DROPDOWN_PAGE.dropdown_menu_dict.values())

	expect(dropdown_page.dropdown_menu_item).to_have_text(expected_items_list)

	dropdown_page.select_option_dropdown_menu(DROPDOWN_PAGE.dropdown_menu_dict['Honda'])

	expect(dropdown_page.dropdown_menu).to_have_value((DROPDOWN_PAGE.dropdown_menu_dict['Honda']).lower())
	expect(dropdown_page.dropdown_menu).not_to_have_value((DROPDOWN_PAGE.dropdown_menu_dict['Ford']).lower())



