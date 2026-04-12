from dataclasses import dataclass


@dataclass(frozen=True)
class DropdownPageData:
	end_point: str
	title: str
	main_header: str
	dropdown_menu_dict: dict


DROPDOWN_PAGE = DropdownPageData(
	end_point="/dropdown",
	title="Dropdown Menus",
	main_header="Dropdown Menus, Radio Buttons & Checkboxes",
	dropdown_menu_dict={
		'Audi': 'Audi',
		'BMW': 'BMW',
		'Ford': 'Ford',
		'Honda': 'Honda',
		'Jeep': 'Jeep',
		'Mercedes': 'Mercedes',
		'Suzuki': 'Suzuki',
		'Volkswagen': 'Volkswagen'
	},
)