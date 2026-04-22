from dataclasses import dataclass


@dataclass(frozen=True)
class BrowserTabPageData:
	end_point: str
	title: str
	main_header: str


BROWSER_TAB_PAGE = BrowserTabPageData(
	end_point="/browserTabs",
	title="Browser Tabs",
	main_header="Browser Tabs",
)
