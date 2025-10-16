from selene import browser, by, be


def test_selene(setup_firefox):
    browser.open("https://github.com")
    browser.element('.input-button').click()
    browser.element('.input-button').send_keys("eroshenkoam/xcresults")
    browser.element('.input-button').press_enter()
    browser.element(by.link_text("eroshenkoam/xcresults")).click()

    browser.element("#issues-tab").click()
    browser.element(by.text('Support for mapping XCTAttachment to Allure labels and environment fields')).should(be.visible)