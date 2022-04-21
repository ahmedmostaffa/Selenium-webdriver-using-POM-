from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Basepage import base_page


class left_menu(base_page):
    ## Locators
    apps_locator=(By.XPATH,'(//a[@jsname="UOtaxb" or @class="mzRh0d"])[2]')
    categories_locator=(By.CSS_SELECTOR,'button.qAAUy')
    Education_locator=(By.LINK_TEXT,'Education')
    search_locator=(By.XPATH,'//input[@class="gbqfif"]')
    Ted_locator=(By.XPATH,"(//div[@class='wXUyZd']/a[@href='/store/apps/details?id=com.ted.android'])[3]")
    
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_apps(self):
        self.driver.find_element(*self.apps_locator).click()

    def click_categories(self):
        self.driver.find_element(*self.categories_locator).click()

    def click_education(self):    
        self.driver.find_element(*self.Education_locator).click()
    
    def search_page(self,text):
        self.driver.find_element(*self.search_locator).send_keys(text + Keys.RETURN)

    def click_TED(self):
        self.driver.find_element(*self.Ted_locator).click()
   


    

        


                               

               




