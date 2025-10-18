from selene import browser, by, be


def test_selene(setup_firefox):
    browser.open("https://github.com")

    browser.element(".search-input").click()
    browser.element("#query-builder-test").type("eroshenkoam/xcresults")
    browser.element("#query-builder-test").press_enter()

    browser.element(by.link_text("eroshenkoam/xcresults")).click()

    browser.element("#issues-tab").click()
    browser.element(by.text('Support for mapping XCTAttachment to Allure labels and environment fields')).should(be.visible)