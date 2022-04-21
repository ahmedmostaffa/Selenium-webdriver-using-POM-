import time
import pytest
from selenium import webdriver
from Pages.movies_page import movies


def test_search_icon(driver):
    page=movies(driver)
    page.load_page('https://play.google.com/store')
    page.click_movies()
    page.implicit_wait(5)
    time.sleep(5)
    assert page.get_title() == 'Movies on Google Play'
    page.scroll_down_inf()
    time.sleep(5)
    page.scroll_down_inf()
    page.wait_element(page.film_locator)
    assert page.click_film() == True

