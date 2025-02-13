import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//span[@class='meni-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_Xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators']"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered']"
    lstitemGuests_xpath = "//li[contains(text(),'Guests']"
    lstitemVendor_xpath = "//li[contains(text(),'Vendors']"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_Xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).sendkeys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).sendkeys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.id, self.txtcustomerRoles_Xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.id,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.id,self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.id, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.id, self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).sendkeys(fname)

    def setLatName(self,lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).sendkeys(lname)

    def setdob(self):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).click()

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).sendkeys(comname)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_Xpath).sendkeys(content)

    def clickOnSave(self):
        self.driver.find_element(By.id, self.btnSave_xpath).click()




