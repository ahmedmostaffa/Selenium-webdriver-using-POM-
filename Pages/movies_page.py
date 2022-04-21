from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Basepage import base_page


class movies(base_page):
    ## Locators
    movies_locator=(By.XPATH,'(//a[@jsname="UOtaxb" or @class="mzRh0d"])[3]')
    search_locator=(By.XPATH,'//input[@class="gbqfif"]')
    film_locator=(By.XPATH,"(//button[@data-item-id='wDyTPSP7KR0.P'])[2]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_movies(self):
        self.driver.find_element(*self.movies_locator).click()    
    
    def search_page(self,text):
        self.driver.find_element(*self.search_locator).send_keys(text + Keys.RETURN)

    def scroll_down(self):
        self.driver.find_element(*self.film_locator).location_once_scrolled_into_view

    def scroll_down_inf(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def click_film(self):
        return self.driver.find_element(*self.film_locator).is_enabled()                  



    

        


                               

               




