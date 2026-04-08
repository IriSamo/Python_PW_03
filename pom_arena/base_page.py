from functools import cached_property

from playwright.sync_api import Page

from pom_arena.header import Header
from pom_arena.side_menu import SideMenu


class BasePage:
	BASE_URL = "https://www.automationtesting.co.uk"

	def __init__(self, page: Page, end_point: str):
		self.page = page
		self.url = self.BASE_URL + end_point
		self._main_body = self.page.locator("#main")

	@cached_property
	def header(self):
		return Header(self.page)

	@cached_property
	def side_menu(self):
		return SideMenu(self.page)

	def open(self):
		self.page.goto(self.url)
		self._main_body.wait_for()
		return self
