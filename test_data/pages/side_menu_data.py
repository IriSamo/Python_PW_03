from dataclasses import dataclass


@dataclass(frozen=True)
class SideMenuData:
    header: str
    labels:tuple


SIDE_MENU_DATA = SideMenuData(
    header="Menu",
    labels=(
        "Homepage",
        "Accordion",
        "Actions",
        "Browser Tabs",
        "Buttons",
        "Calculator (JS)",
        "Contact Us Form Test",
        "Date Picker",
        "DropDown Checkbox Radio",
        "File Upload",
        "Hidden Elements",
        "iFrames",
        "Loader",
        "Loader Two",
        "Login Portal Test",
        "Mouse Movement",
        "Pop Ups & Alerts",
        "Predictive Search",
        "Tables",
        "Test Store",
        "About Me",
    )
)