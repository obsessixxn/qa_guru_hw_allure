import allure
from allure_commons.types import Severity
from selene import browser, by, be


def test_github_with_decorators(setup_firefox):
    allure.dynamic.tag("web", "ui", "smoke")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Github repo")
    allure.dynamic.story("Looking for repo with issue")
    allure.dynamic.link("https://github.com", name="github repo")

    open_main_page()
    looking_for_repo("eroshenkoam/xcresults")
    go_to_repo("eroshenkoam/xcresults")
    go_to_issue()
    check_issue_with_name("Support for mapping XCTAttachment to Allure labels and environment fields")


@allure.step("Open main page")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Looking for {repo}")
def looking_for_repo(repo):
    browser.element(".search-input").click()
    browser.element("#query-builder-test").type(repo)
    browser.element("#query-builder-test").press_enter()


@allure.step("Go to repo {repo}")
def go_to_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Go to issue")
def go_to_issue():
    browser.element("#issues-tab").click()


@allure.step("Check for issue with name {title}")
def check_issue_with_name(title):
    browser.element(by.text(title)).should(be.visible)
