import pytest

from pom_arena.accordion_page import AccordionPage
from pom_arena.home_page import HomePage
from pom_arena.loader_page import LoaderPage


@pytest.fixture
def home_page(page):
	return HomePage(page)


@pytest.fixture
def accordion_page(page):
	return AccordionPage(page)


@pytest.fixture
def loader_page(page):
	return LoaderPage(page)