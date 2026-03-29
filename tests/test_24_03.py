import re
from playwright.sync_api import Page, expect


def test_getting_started_list_sidebar(page:Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    # getting_started_btn = page.get_by_role('button', name = 'Getting Started', exact = True)
    # getting_started_list = page.locator('.menu__list-item').filter( has = page.get_by_text(re.compile(r"^Getting Started$" )))
    # getting_started_list = page.locator('.menu__list-item').filter(
    #     has=page.get_by_text("Getting Started", exact = True))
    # getting_started_list = page.get_by_role('navigation').get_by_role('listitem').filter( has = page.get_by_role( 'button', name = re.compile(r"^Getting Started$" )))
    getting_started_list = page.get_by_role('listitem').filter( has=page.get_by_role('button', name="Getting Started", exact = True))
    getting_started_list_item = getting_started_list.get_by_role('listitem')

    expected_list_items = ['Installation', 'Writing tests', 'Generating tests', 'Running and debugging tests', 'Trace viewer', 'Setting up CI']
    counter = len(expected_list_items)

    expect(getting_started_list).to_be_visible()
    # print(getting_started_list.inner_text())
    expect(getting_started_list).to_contain_text("Installation")
    expect(getting_started_list_item).to_have_count(counter)

    for i in range(counter):
        expect(getting_started_list_item.nth(i)).to_have_text(expected_list_items[i])