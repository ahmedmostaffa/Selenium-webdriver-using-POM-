import time
from Pages.Search_Page import search_page
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d=webdriver.Chrome()
    d.implicitly_wait(10)
    yield d
    d.quit()

def test_search_icon(driver):
    page=search_page(driver)
    page.load_page('https://play.google.com/store')
    page.search_home_page('facebook')
    time.sleep(5)
    assert page.icon_exist() == True 
