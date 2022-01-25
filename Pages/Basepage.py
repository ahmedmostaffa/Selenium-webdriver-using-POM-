from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class base_page:
    
    def __init__(self,driver):
        self.driver=driver

    def load_page(self,URL):
        self.driver.get(URL) 

    def wait_element(self,*locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(*locator))    

    def get_current_url(self):
        return (self.driver.current_url)

    def get_title(self):
        return (self.driver.title)    


        
        


        


    

        


                               

               




