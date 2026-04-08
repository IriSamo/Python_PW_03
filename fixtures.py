import pytest

from pom_arena.accordion_page import AccordionPage
from pom_arena.home_page import HomePage


@pytest.fixture
def home_page(page):
	return HomePage(page)


@pytest.fixture
def accordion_page(page):
	return AccordionPage(page)
