from selenium.webdriver.common.by import By

from browser import Browser



class LoginPage(Browser):

    USERNAME_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[1]/input')
    PASSWORD_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[2]/input')
    LOGIN_BUTTON_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input')
    MESSAGE_ERROR_LABEL = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/p')



    def navigate_to_login_page(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

    def enter_username(self, jhon1234):
        self.driver.find_element(*self.USERNAME_FIELD_SELECTOR).send_keys(jhon1234)

    def enter_password(self, demo):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(demo)


    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LABEL).text
