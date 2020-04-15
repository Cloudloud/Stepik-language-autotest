from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_basket_btn_exist(browser):
    try:
        browser.get(link)
        WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
                )
        basket=browser.find_elements_by_css_selector(".btn-a2dd-to-2basket")
        assert len(basket)==1, 'Кнопка корзины отсутствует'
    except TimeoutException:
        raise AssertionError('Кнопка не видна на странице')