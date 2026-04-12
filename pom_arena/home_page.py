from functools import cached_property

from pom_arena.base_page import BasePage


class HomePage(BasePage):
	END_POINT = "/index.html"

	def __init__(self, page):
		super().__init__(page, self.END_POINT)

	@cached_property
	def main_header(self):
		return self._main_body.locator('h1')
