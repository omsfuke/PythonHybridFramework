import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utiities.readProperties import ReadConfig
from Utiities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # Test caes 1
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        # self.driver = webdriver.Chrome()

        self.logger.info("__________Test_001_Login____________")
        self.logger.info("___________Verify home page title_______________")

        self.driver = setup
        self.driver.get(self.baseUrl)

        act_title = self.driver.title
        print(act_title)

        # self.driver.close()
        if act_title == "Your store. Login":
            self.logger.info("-----------Home page title test is pass-------------------")
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.error("-----------Home page title test is fail-------------------")
            assert False
            self.driver.close()

    # Test caes 2
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        # self.driver = webdriver.Chrome()
        self.logger.info("------Verifyinh login test----")

        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        self.driver.implicitly_wait(100)
        print(act_title)
        self.driver.close()
        '''
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("------login test pass----")
            
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("------login test fail----")
            assert False
            '''
