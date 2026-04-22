import yaml

import pytest
from playwright.sync_api import Page, expect, Locator

from test_data.credentials import credentials


def load_yaml():
	with open("test_data/login.yaml") as f:
		return yaml.safe_load(f)


class TestOrangeLogin:

	@pytest.mark.parametrize(
		"username, password",
		[
			("user1", "pass1"),
			("user2", "wrong"),
		]
	)
	def test_login(self, page: Page, username: str, password: str):
		page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
		page.get_by_role("textbox", name="Username").fill(username)
		page.get_by_role("textbox", name="Password").fill(password)
		page.get_by_role("button", name="Login").click()

		expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")

	@pytest.mark.parametrize("username, password", credentials)
	def test_login(self, page: Page, username: str, password: str):
		page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
		page.get_by_role("textbox", name="Username").fill(username)
		page.get_by_role("textbox", name="Password").fill(password)
		page.get_by_role("button", name="Login").click()

		expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")

	@pytest.mark.parametrize("data", load_yaml())
	def test_login(self, page: Page, data: dict[str, str]):
		page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
		page.get_by_role("textbox", name="Username").fill(data["username"])
		page.get_by_role("textbox", name="Password").fill(data["password"])
		page.get_by_role("button", name="Login").click()

		expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")
