from dataclasses import dataclass


@dataclass(frozen=True)
class AccordionPageData:
	end_point: str
	title: str
	main_header: str


ACCORDION_PAGE = AccordionPageData(
	end_point="/accordion",
	title="Accordion",
	main_header="Accordion Test",
)
