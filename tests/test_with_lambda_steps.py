import allure
from selene import browser, by, be
from allure_commons.types import Severity


def test_with_lambda_steps(setup_firefox):
    allure.dynamic.tag("web", "ui", "smoke")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Github repo")
    allure.dynamic.story("Looking for repo with issue")
    allure.dynamic.link("https://github.com", name="github repo")

    with allure.step('Open github'):
        browser.open('https://github.com')
    with allure.step('Searching for repository'):
        browser.element(".search-input").click()
        browser.element("#query-builder-test").type("eroshenkoam/xcresults")
        browser.element("#query-builder-test").press_enter()
    with allure.step('go to repository'):
        browser.element(by.link_text("eroshenkoam/xcresults")).click()
    with allure.step('go to issues'):
        browser.element("#issues-tab").click()
    with allure.step('looking for our issue'):
        browser.element(by.text('Support for mapping XCTAttachment to Allure labels and environment fields')).should(
            be.visible)
