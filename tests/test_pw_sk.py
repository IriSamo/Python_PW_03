import re
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="function", autouse=True)
def before_each_function(page: Page):
    page.goto("https://playwright.dev/python/")
    page.get_by_role("link", name="Get started").click()

def test_getting_started_list_sidebar(page: Page):

    # getting_started_btn = page.get_by_role('button', name = 'Getting Started', exact = True)
    #getting_started_list = page.locator('.menu__list-item').filter( has = page.get_by_text(re.compile(r"^Getting Started$" )))
    # getting_started_list = page.locator('.menu__list-item').filter(
    #     has=page.get_by_text("Getting Started", exact = True))
    # getting_started_list = page.get_by_role('navigation').get_by_role('listitem').filter( has = page.get_by_role( 'button', name = re.compile(r"^Getting Started$" )))
    getting_started_list = page.get_by_role('listitem').filter(
        has=page.get_by_role('button', name="Getting Started", exact=True))
    # getting_started_list = page.locator('.theme-doc-sidebar-container li ul.menu__list').filter( has_not_text= 'Getting started - Library' ).nth(0)
    getting_started_list_item = getting_started_list.get_by_role('listitem')

    expected_list_items = ['Installation', 'Writing tests', 'Generating tests', 'Running and debugging tests',
                           'Trace viewer', 'Setting up CI', 'Pytest Plugin Reference']
    counter = len(expected_list_items)

    expect(getting_started_list).to_be_visible()
    print(getting_started_list.inner_text())
    expect(getting_started_list).to_contain_text("Installation")
    # expect(getting_started_list_item).to_have_count(counter)

    for i in range(counter):
        expect(getting_started_list_item.nth(i)).to_have_text(expected_list_items[i])


def test_hiding_sidebar(page: Page):
    getting_started_btn = page.get_by_role('button', name='Getting Started', exact=True)
    getting_started_list = page.locator('.menu__list-item').filter(
        has=page.get_by_text(re.compile(r"^Getting Started$")))
    getting_started_list_item = getting_started_list.get_by_role('listitem')

    expect(getting_started_list_item.nth(1)).to_be_visible()

    getting_started_btn.click()

    expect(getting_started_list_item.nth(1)).not_to_be_visible()


def test_scrolling(page: Page):
    getting_started_list = page.get_by_role('listitem').filter(
        has=page.get_by_role('button', name="Getting Started", exact=True))

    writing_test_sidebar = getting_started_list.get_by_text("Writing tests")

    writing_test_sidebar.click()

    # python automatically scroll for you before doing any actions
    basic_actions_header = page.get_by_role('heading', name = "Basic actions")

    # in rare cases you might need to manually scroll
    # basic_actions_header.scroll_into_view_if_needed()
    expect(basic_actions_header).to_be_visible()

def test_basic_actions_table(page: Page):
    getting_started_list = page.get_by_role('listitem').filter(
        has=page.get_by_role('button', name="Getting Started", exact=True))
    writing_test_sidebar = getting_started_list.get_by_text("Writing tests")
    writing_test_sidebar.click()
    basic_actions_header = page.get_by_role('heading', name="Basic actions")

    basic_actions_table = page.get_by_role('table').filter( has_text = "Check the input checkbox")
    expect(basic_actions_table).to_be_visible()

    table_header = basic_actions_table.locator('th')
    print(table_header.all_inner_texts())

    expected_table_header = ['Action', 'Description']

    expect(table_header).to_have_text(expected_table_header)

    table_action_body = basic_actions_table.locator('td a')
    table_description_body = basic_actions_table.locator('td').filter( has_not = page.locator('a'))

    expected_table_action_body = [
        'locator.check()',
        'locator.click()',
        'locator.uncheck()',
        'locator.hover()',
        'locator.fill()',
        'locator.focus()',
        'locator.press()',
        'locator.set_input_files()',
        'locator.select_option()'
    ]
    expected_table_description_body = [
        'Check the input checkbox',
        'Click the element',
        'Uncheck the input checkbox',
        'Hover mouse over the element',
        'Fill the form field, input text',
        'Focus the element',
        'Press single key',
        'Pick files to upload',
        'Select option in the drop down'
    ]
    count = len(expected_table_action_body)

    for i in range(count):
        expect(basic_actions_table.locator('td a').nth(i)).to_have_text(expected_table_action_body[i])
        assert table_action_body.nth(i).inner_text() == expected_table_action_body[i]
        assert table_description_body.nth(i).inner_text() == expected_table_description_body[i]

    keys = []
    values = []
    actual_table_body = {}
    for i in range(count):
        actual_table_body[table_action_body.nth(i).inner_text()] = table_description_body.nth(i).inner_text()
        keys.append(expected_table_action_body[i])
        values.append(expected_table_description_body[i])

    print(table_action_body.nth(0).inner_text())
    print(actual_table_body)
    expected_table_dict = dict(zip(keys, values))
    print(expected_table_dict)

    assert actual_table_body == expected_table_dict

def test_dropdown_header(page: Page):
    dropdown_header_btn = page.locator('.dropdown ')
    dropdown_header_list = dropdown_header_btn.locator('ul > li > a')

    dropdown_header_btn.hover()

    expect(dropdown_header_list).to_have_count(4)
    expect(dropdown_header_list).to_have_text(['Python', 'Node.js', 'Java', '.NET'])










