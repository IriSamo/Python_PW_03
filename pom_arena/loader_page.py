from functools import cached_property

from pom_arena.base_page import BasePage


class LoaderPage(BasePage):
	END_POINT = "/loader.html"

	def __init__(self, page):
		super().__init__(page, self.END_POINT)


	@cached_property
	def main_header(self):
		return self._main_body.locator('h2', has_text="Loader")

	@cached_property
	def loader(self):
		return self._main_body.locator("#loader")

	@cached_property
	def loading_complete_message(self):
		return self._main_body.get_by_text("Loading Complete")

