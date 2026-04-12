from functools import cached_property

from playwright.sync_api import Page


class Header:

	def __init__(self, page: Page):
		self.page = page
		self._header = page.locator("#header")

	@cached_property
	def logo(self):
		return self._header.locator('.logo')
