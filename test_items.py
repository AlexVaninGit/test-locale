from selenium.webdriver.common.by import By


def test_locale(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert button.is_displayed(), 'expected: "button in page", actual: "button not page"'