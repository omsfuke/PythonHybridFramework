import string

import pytest
from selenium import webdriver
import random

from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from Utiities.readProperties import ReadConfig
from Utiities.customLogger import LogGen


class Test_003_Login:
    baseUrl = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    # Test caes 2
    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        # self.driver = webdriver.Chrome()
        self.logger.info("-----Test_003_AddCustomer----")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************Log in successfull****")

        self.lp.driver("****Starting Add customer Test******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerManu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.lp.driver("****Proving customer info ******")

        self.email = random_generator() + "gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pavan")
        self.addcust.setLatName("Kumar")
        self.addcust.setdob("7/5/1999")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing..")
        self.addcust.clickOnSave()

        self.lp.driver("*** Saving customer info ******")

        self.lp.driver("**** Add customer validation ******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been  added successfully.' in self.msg:
            assert True == True
            self.lp.driver("**** Add customer test passed ******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_Scr.png")
            self.lp.driver("**** Add customer test failed ******")
            assert True == False

        self.driver.close()
        self.lp.driver("**** Ending home page title test ******")



def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return ' '.join(random.choice(char) for x in random(size))


