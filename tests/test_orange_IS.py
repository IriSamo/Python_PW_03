import re
import time

import pytest
from playwright.sync_api import Page, expect, Locator


@pytest.fixture(scope="function", autouse=True)
def before_each_function(page: Page):
	page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
	page.get_by_role("textbox", name="Username").fill("Admin")
	page.get_by_role("textbox", name="Password").fill("admin123")
	page.get_by_role("button", name="Login").click()


def test_has_title(page: Page):
	expect(page).to_have_url(re.compile("/dashboard/index"))
	expect(page).to_have_title("OrangeHRM")
	expect(page.get_by_role("heading")).to_contain_text("Dashboard")


def test_sidepanel_change_size_by_class(page: Page):
	sidepanel = page.locator("aside")

	expect(sidepanel).not_to_have_class(re.compile("toggled"))

	sidepanel.get_by_role("button").click()

	expect(sidepanel).to_have_class(re.compile("toggled"))


def test_sidepanel_change_size_by_css(page: Page):
	sidepanel = page.get_by_role("navigation", name="Sidepanel")

	expect(sidepanel).to_have_css("width", "256px")
	expect(sidepanel).to_have_css("height", "720px")

	sidepanel.get_by_role("button").click()

	expect(sidepanel).to_have_css("width", "83.1875px")
	expect(sidepanel).to_have_css("width", re.compile(r"83(\.\d+)?px"))
	expect(sidepanel).to_have_css("height", "720px")


def test_sidepanel_change_size_by_evaluate(page: Page):
	sidepanel = page.get_by_role("navigation", name="Sidepanel")

	size = element_size(sidepanel)
	assert size["width"] == 256
	assert size["height"] == 720
	assert list(size.values()) == [256, 720]

	sidepanel.get_by_role("button").click()

	wait_for_size_stable(sidepanel)

	size = element_size(sidepanel)
	assert size["width"] == 83
	assert size["height"] == 720
	assert list(size.values()) == [83, 720]


def element_size(locator: Locator) -> dict[str, int]:
	box = locator.bounding_box()

	return {
		"width": int(box["width"]),
		"height": int(box["height"]),
	}


def wait_for_size_stable(locator: Locator, stable_duration: float = 0.5, poll_interval: float = 0.25, timeout: float = 3.0):
	deadline = time.monotonic() + timeout
	last_size = None
	stable_since = None

	handle = locator.element_handle()
	if handle is None:
		raise RuntimeError("Element handle is not available")

	while True:
		now = time.monotonic()
		if now > deadline:
			raise TimeoutError(f"Element size did not stabilize within {timeout} seconds")

		size = handle.evaluate("el => ({width: el.getBoundingClientRect().width, height: el.getBoundingClientRect().height})")

		if size == last_size:
			if stable_since is None:
				stable_since = now
			elif now - stable_since >= stable_duration:
				return size
		else:
			last_size = size
			stable_since = None

		time.sleep(poll_interval)
