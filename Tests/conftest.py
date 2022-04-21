
from msilib.schema import Directory
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
"""
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
"""



def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome")
    #parser.addoption("--headless",action="store",default=False)
"""
@pytest.fixture(autouse=True)
def get_browser(request):
    data={}
    data['browser_cmd']=request.config.getoption("--browser")
    data['browser_cmd']=request.config.getoption("--headless")
    return data
"""


@pytest.fixture(autouse=True)
def get_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(autouse=True)
def driver(request,get_browser):
    if get_browser =='chrome'  or get_browser =='Chrome':
        """"
        d=webdriver.Chrome()
        d.implicitly_wait(10)
        yield d
        d.quit()
        """
        print('hello chrome')
    elif get_browser =='firefox' or get_browser =='Firefox':
        d=webdriver.Firefox()
        d.implicitly_wait(10)
        yield d
        d.quit()






    


