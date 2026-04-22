import pytest

from pom_arena.accordion_page import AccordionPage
from pom_arena.home_page import HomePage
from pom_arena.loader_page import LoaderPage
from pom_arena.contact_form_page import ContactFormPage
from pom_arena.dropdown_page import DropdownPage


@pytest.fixture
def home_page(page):
	return HomePage(page)


@pytest.fixture
def accordion_page(page):
	return AccordionPage(page)


@pytest.fixture
def loader_page(page):
	return LoaderPage(page)


@pytest.fixture
def dropdown_page(page):
	return DropdownPage(page)


@pytest.fixture
def contact_form_page(page):
	return ContactFormPage(page).open()