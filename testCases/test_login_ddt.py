import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utiities.readProperties import ReadConfig
from Utiities.customLogger import LogGen
from Utiities import XLUtils


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = "./TestData/Login.xlsx"

    logger = LogGen.loggen()

    # Test caes 1
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        # self.driver = webdriver.Chrome()
        self.logger.info("------Test_002_DDT_Login----")
        self.logger.info("------Verifying login DDT test----")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)

        lat_status=[]


        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerse administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** passed *")
                    self.lp.clickLogout()
                    lat_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*** Failed *")
                    self.lp.clickLogout()
                    lat_status.append("fail")
            if act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** failed *")
                    self.lp.clickLogout()
                    lat_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*** Pass *")
                    self.lp.clickLogout()
                    lat_status.append("Pass")
            if "Fail" not in lat_status:
                self.logger.info("Login DDT test passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("Login DDT test failed")
                self.driver.close()
                assert False

        self.logger.info("********End of Login DDT Test*******")
        self.logger.info("********Complete TC_lOGINDDT_002*******")








