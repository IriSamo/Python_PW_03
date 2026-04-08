from dataclasses import dataclass


@dataclass(frozen=True)
class SideMenuData:
    header: str


SIDE_MENU_DATA = SideMenuData(
    header="Menu",
)