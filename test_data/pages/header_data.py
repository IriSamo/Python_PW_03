from dataclasses import dataclass


@dataclass(frozen=True)
class HeaderData:
	logo_text: str


HEADER_DATA = HeaderData(
	logo_text="Automation Testing Test Arena"
)