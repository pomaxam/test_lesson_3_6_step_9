import time

def test_browser_language_and_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "Кнопка не найдена"
    time.sleep(10)