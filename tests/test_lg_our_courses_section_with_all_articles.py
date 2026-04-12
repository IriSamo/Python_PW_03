from playwright.sync_api import Page, expect

def test_our_courses_all_9(page : Page):
    page.goto("https://www.automationtesting.co.uk/")
    header_courses = page.locator("h3" , has_text="Our Courses:")

    expect(header_courses).to_be_visible()

    print("'Our Courses:' header is visible")

    COURSES_EXPECTED = [
        "API Testing in Detail!",
        "Cypress with Cucumber BDD!",
        "Selenium Webdriver & Java!",
        "Cucumber BDD with Selenium & Java!",
        "Cypress.io 10 using Javascript!",
        "Webdriver IO using Javascript!",
        "Mastering Selectors/Locators!",
        "Selenium Webdriver 4 - New Features!",
        "Intro to Cucumber BDD, Selenium & Java (Free - 2.5hrs)!",
    ]


    articles = page.locator("article")
    expect(articles).to_have_count(len(COURSES_EXPECTED))

    for course in COURSES_EXPECTED:

        course_title = page.locator("article").filter(has_text=course)
        expect(course_title).to_be_visible()
        expect (course_title).to_contain_text(course)
        print(f"'{course}' is visible")







