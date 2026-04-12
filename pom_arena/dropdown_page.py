from functools import cached_property

from pom_arena.base_page import BasePage


class DropdownPage(BasePage):
	END_POINT = "/dropdown.html"

	def __init__(self, page):
		super().__init__(page, self.END_POINT)

	@cached_property
	def main_header(self):
		return self._main_body.locator('h2', has_text="Dropdown Menus, Radio Buttons & Checkboxes")

	@cached_property
	def dropdown_menu(self):
		return self._main_body.locator('#cars')

	@cached_property
	def dropdown_menu_item(self):
		return self.dropdown_menu.locator('option')

	def click_dropdown_menu(self):
		self.dropdown_menu.click()

	def select_option_dropdown_menu(self, option):
		self.dropdown_menu.select_option(option)


