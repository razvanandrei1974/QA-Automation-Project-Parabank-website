from selenium.webdriver.common.by import By

from browser import Browser


class RegisterPage(Browser):
    # LOGOUT_BUTTON_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul/li[8]/a')
    REGISTER_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#loginPanel > p:nth-child(3) > a')
    FIRSTNAME_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input')
    LASTNAME_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[2]/td[2]/input')
    ADRESS_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/input')
    CITY_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[4]/td[2]/input')
    STATE_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[5]/td[2]/input')
    ZIPCODE_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[6]/td[2]/input')
    PHONE_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[7]/td[2]/input')
    SSN_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[8]/td[2]/input')
    USER_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[10]/td[2]/input')
    PASSW_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[11]/td[2]/input')
    CONFIRM_FIELD_SELECTOR = (By.CSS_SELECTOR, '#repeatedPassword')
    REGISTER1_BUTTON_SELECTOR = (By.CSS_SELECTOR, '#customerForm > table > tbody > tr:nth-child(13) > td:nth-child(2) > input')
    MESSAGE_LABEL = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[10]/td[3]/span')

    def navigate_to_register_page(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

    # def click_logout_button(self):
    #     self.driver.find_element(*self.LOGOUT_BUTTON_SELECTOR).click()

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON_SELECTOR).click()

    def enter_firstname(self, Razvan):
        self.driver.find_element(*self.FIRSTNAME_FIELD_SELECTOR).send_keys(Razvan)

    def enter_lastname(self, Ungar):
        self.driver.find_element(*self.LASTNAME_FIELD_SELECTOR).send_keys(Ungar)

    def enter_adress(self, Ciocarliei):
        self.driver.find_element(*self.ADRESS_FIELD_SELECTOR).send_keys(Ciocarliei)

    def enter_city(self, Resita):
        self.driver.find_element(*self.CITY_FIELD_SELECTOR).send_keys(Resita)

    def enter_state(self, CarasSeverin):
        self.driver.find_element(*self.STATE_FIELD_SELECTOR).send_keys(CarasSeverin)

    def enter_zipcode(self, Z320038):
        self.driver.find_element(*self.ZIPCODE_FIELD_SELECTOR).send_keys(Z320038)

    def enter_phone(self, P0726165557):
        self.driver.find_element(*self.PHONE_FIELD_SELECTOR).send_keys(P0726165557)

    def enter_ssn(self, SSN1740827354807):
        self.driver.find_element(*self.SSN_FIELD_SELECTOR).send_keys(SSN1740827354807)

    def enter_user(self, user):
        self.driver.find_element(*self.USER_FIELD_SELECTOR).send_keys(user)

    def enter_passw(self, passw):
        self.driver.find_element(*self.PASSW_FIELD_SELECTOR).send_keys(passw)

    def enter_confirm_pass(self, confirm):
        self.driver.find_element(*self.PASSW_FIELD_SELECTOR).send_keys(confirm)

    def click_register1_button(self):
        self.driver.find_element(*self.REGISTER1_BUTTON_SELECTOR).click()



    def get_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LABEL).text
