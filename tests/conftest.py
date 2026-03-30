import os
from dotenv import load_dotenv
from pathlib import Path
import pytest

load_dotenv()

# -----------------------------
# PROJECT ROOT
# -----------------------------
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# -----------------------------
# ARTIFACTS DIRS
# -----------------------------
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
TRACES_DIR = ARTIFACTS_DIR / "traces"
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
REPORTS_DIR = ARTIFACTS_DIR / "reports"
HTML_REPORT_PATH = REPORTS_DIR / "report.html"
XML_REPORT_PATH = REPORTS_DIR / "report.xml"

# -----------------------------
# CONFIG FROM ENV
# -----------------------------
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", 0))
VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", 1280))
VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", 720))
LOCALE = os.getenv("LOCALE", "en-UK")
TIMEZONE_ID = os.getenv("conftest.py", "Europe/London")


# -----------------------------
# PYTEST HTML REPORT CONFIG
# -----------------------------
def pytest_configure(config):
	REPORTS_DIR.mkdir(parents=True, exist_ok=True)

	config.option.htmlpath = str(HTML_REPORT_PATH)
	config.option.self_contained_html = True


# -----------------------------
# BROWSER CONFIG
# -----------------------------
@pytest.fixture(scope="session")
def browser_type_launch_args():
	return {
		"headless": HEADLESS,
		"slow_mo": SLOW_MO
	}


# -----------------------------
# CONTEXT CONFIG
# -----------------------------
@pytest.fixture(scope="session")
def browser_context_args():
	return {
		"viewport": {
			"width": VIEWPORT_WIDTH,
			"height": VIEWPORT_HEIGHT
		},
		"locale": LOCALE,
		"timezone_id": TIMEZONE_ID,
	}


# -----------------------------
# TRACE PER TEST
# -----------------------------
@pytest.fixture(autouse=True)
def setup_tracing(context, request):
	TRACES_DIR.mkdir(parents=True, exist_ok=True)

	context.tracing.start(
		screenshots=True,
		snapshots=True,
		sources=True,
	)

	yield

	test_name = request.node.nodeid.replace("::", "_").replace("/", "_")[:100]
	trace_path = TRACES_DIR / f"{test_name}.zip"
	context.tracing.stop(path=str(trace_path))


# -----------------------------
# SCREENSHOT ON FAILURE
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
	outcome = yield
	report = outcome.get_result()

	if report.when != "call" or not report.failed:
		return

	page = item.funcargs.get("page")
	if not page:
		return

	SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

	test_name = report.nodeid.replace("::", "_").replace("/", "_")[:100]
	screenshot_filename = f"{test_name}.png"
	screenshot_path = SCREENSHOTS_DIR / screenshot_filename

	page.screenshot(path=str(screenshot_path))

	relative_path_for_report = f"../screenshots/{screenshot_filename}"

	from pytest_html import extras

	report.extras = getattr(report, "extras", [])
	report.extras.append(extras.image(relative_path_for_report))
