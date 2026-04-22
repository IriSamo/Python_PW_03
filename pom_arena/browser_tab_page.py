from functools import cached_property

from pom_arena.base_page import BasePage


class BrowserTabPage(BasePage):
	END_POINT = "/browserTabs.html"

	def __init__(self, page):
		super().__init__(page, self.END_POINT)


	@cached_property
	def main_header(self):
		return self._main_body.locator('h2', has_text="Browser Tabs")

	@cached_property
	def open_tab_btn(self):
		return self._main_body.locator('.row input')

	def click_open_tab_btn(self):
		self.open_tab_btn.click()