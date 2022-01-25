from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Basepage import base_page


class search_page(base_page):
    ## Locators
    search_locator=(By.XPATH,'//input[@class="gbqfif"]')
    icon_locator=(By.XPATH,'(//a[@href="/store/apps/details?id=com.facebook.katana"])[1]')
    
    def __init__(self, driver):
        super().__init__(driver)

    def search_home_page(self,text):
        self.driver.find_element(*self.search_locator).send_keys(text + Keys.RETURN)

    def icon_exist(self):
        return (self.driver.find_element(*self.icon_locator).is_displayed())   
    

