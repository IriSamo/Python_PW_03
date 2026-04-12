from dataclasses import dataclass


@dataclass(frozen=True)
class HomePageData:
	end_point: str
	title: str
	main_header: str


HOME_PAGE = HomePageData(
	end_point="/index",
	title="Homepage",
	main_header=" Testing Arena",
)