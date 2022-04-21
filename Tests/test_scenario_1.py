import time
from Pages.Left_Menu import left_menu
import pytest
from selenium import webdriver


def test_left_menu(driver):
    page=left_menu(driver)
    page.load_page('https://play.google.com/store')
    page.click_apps()
    time.sleep(5)
    assert page.get_title() == 'Android Apps on Google Play'
    page.wait_element(page.categories_locator)
    page.click_categories()
    time.sleep(5)
    page.click_education()
    time.sleep(5)
    assert page.get_title() == 'Education - Android Apps on Google Play'
    page.search_page('TED')
    page.wait_element(page.Ted_locator)
    page.click_TED()
    time.sleep(5)
    assert page.get_title() == 'TED - Apps on Google Play'
    







       

    


    



