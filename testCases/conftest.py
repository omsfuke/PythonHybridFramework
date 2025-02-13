import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        print("----Launching chrome browser-----------")
    elif browser == 'firefox':
        service_obj = Service("C:\Drivers\geckodriver-v0.35.0-win32\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()
        print("----Launching firefox browser-----------")
    elif browser == 'edgebrowser':
        service_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.maximize_window()
        print("----Launching firefox browser-----------")
    else:
        service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        print("----Launching chrome browser-----------")
    return driver


def pytest_addoption(parser):  # This will get value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # return browser value to setup method
    return request.config.getoption("--browser")


################ Pttest HTML Report

