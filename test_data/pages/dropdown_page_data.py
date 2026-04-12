from dataclasses import dataclass


@dataclass(frozen=True)
class DropdownPageData:
	end_point: str
	title: str
	main_header: str
	dropdown_menu_list: list


DROPDOWN_PAGE = DropdownPageData(
	end_point="/dropdown",
	title="Dropdown Menus",
	main_header="Dropdown Menus, Radio Buttons & Checkboxes",
	dropdown_menu_list=['Audi', 'BMW', 'Ford', 'Honda', 'Jeep', 'Mercedes', 'Suzuki', 'Volkswagen'],
)