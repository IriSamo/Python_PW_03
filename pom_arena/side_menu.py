from functools import cached_property

from playwright.sync_api import Page


class SideMenu:

	def __init__(self, page: Page):
		self.page = page
		self._side_menu = page.locator("#sidebar")

	@cached_property
	def main_header(self):
		return self._side_menu.locator('h2')

	def click_item(self, text: str):
		self._side_menu.locator(f"text={text}").click()

	def clik_accordion(self):
		from pom_arena.accordion_page import AccordionPage
		with self.page.expect_navigation():
			self._side_menu.locator("text=Accordion").click()
		return AccordionPage(self.page)

	def get_menu_link(self, text: str):
		return self._side_menu.locator("ul li a").filter(has_text=text).first
