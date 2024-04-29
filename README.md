# QA-Automation-Project-Parabank-website 🔄

📍 Am creat planul de testare automată cu Behave pentru meniul de _"Login"_ și meniul _"Register"_ pentru aplicația Parabank. 
📍 Am folosit Selenium pentru a automatiza acțiunile de navigare și interacțiune cu interfața web. 

## 📌 Instalare și configurare:

🖥️ Am instalat Behave, Selenium, WebDriver pentru Python.

▶️ Definirea scenariilor de testare:

Se deschide un fișier _.feature_ pentru a defini scenariile de testare, atat pentru meniul **Login** cat și pentru **Register**.
Am definit scenariile de testare pentru diferite cazuri de utilizare, cum ar fi:

▶️ Login cu succes utilizând credențiale valide.
```markdown
```python
Feature: Login Feature

  Background:
    Given I am on the login page

  @first
  Scenario: Login with wrong credentials

    When I enter "jhon1234" in username field
    And I enter "demo" in password field
    And I press the login button
    Then I should see an error message


▶️ Login eșuat cu credențiale invalide.

Validarea mesajelor de eroare pentru câmpurile obligatorii la login și înregistrare.
Înregistrare cu succes cu date valide.
Înregistrare eșuată cu date invalide.
📩 Implementarea pasilor de testare:

Pentru fiecare scenariu definit în fișierul .feature, implementează pașii de testare în fișierul steps.py.
```markdown
```python
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


Folosește Selenium pentru a automatiza acțiunile de navigare și interacțiune cu elementele din interfața web.
Exemplu de pași de testare pentru login ar putea fi:
Navigare către pagina de login.
Introducerea numelui de utilizator și a parolei.
Apăsarea butonului de login.
Validarea succesului sau eșecului login-ului în funcție de rezultatul așteptat.

```markdown
import time

from behave import *


@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()


@when('I enter "{jhon1234}" in username field')
def step_impl(context, jhon1234):
    context.LoginPage.enter_username(jhon1234)
    time.sleep(3)


@when('I enter "{demo}" in password field')
def step_impl(context, demo):
    context.LoginPage.enter_password(demo)


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_error_message = 'The username and password could not be verified.'
    assert expected_error_message in actual_error_message


@when('I press the login button')
def steps_impl(context):
    context.LoginPage.click_login_button()
```

### 📌 _Rularea testelor:_
![image](https://github.com/razvanandrei1974/QA-Automation-Project-Parabank-website/assets/144438182/d02d5f8c-a126-4376-bbb7-a3a7362049f4)


### _Raportare și remediere:_
Dupa rularea testestelor din doua scenarii:
  * Dupa rularea testelor pe meniul Login am raportat 5/5 teste passed .
  

# 📌 Pentru testarea meniului REGISTER am parcurs urmatorii pasi:

## 📌 Am creat register.feature

```
markdown
Feature: Register Feature

  Background:
    Given I am on the register page

  @second
  Scenario: Register with corect credentials

    When I press the logout button
    When I press the register button
    And I enter "Razvan" in FirstName field
    And I enter "Ungar" in LastName field
    And I enter "Ciocarliei" in Adress field
    And I enter "Resita" in City field
    And I enter "CarasSeverin" in State field
    And I enter "Z320038" in Zip Code field
    And I enter "P0726165557" in Phone field
    And I enter "SSN1740827354807" in SSN field
    And I enter "Razvan1199774420241" in User field
    And I enter "P123456789" in Passw field
    And I enter "P123456789" in Confirm field
    And I press the register1 button
    Then I should see an error message
```

## 📌 Am creat register_page .

```
markdown
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
```
## 📌 Am creat steps_register

```
markdown
import time

from behave import *


@given('I am on the register page')
def step_impl(context):
    context.RegisterPage.navigate_to_register_page()

# @when('I press the logout button')
# def steps_impl(context):
#     context.RegisterPage.click_logout_button()

@when('I press the register button')
def steps_impl(context):
    context.RegisterPage.click_register_button()


@when('I enter "{Razvan}" in FirstName field')
def step_impl(context, Razvan):
    context.RegisterPage.enter_firstname(Razvan)
    time.sleep(2)

@when('I enter "{Ungar}" in LastName field')
def step_impl(context, Ungar):
    context.RegisterPage.enter_lastname(Ungar)
    time.sleep(2)

@when('I enter "{Ciocarliei}" in Adress field')
def step_impl(context, Ciocarliei):
    context.RegisterPage.enter_adress(Ciocarliei)
    time.sleep(2)

@when('I enter "{Resita}" in City field')
def step_impl(context, Resita):
    context.RegisterPage.enter_city(Resita)
    time.sleep(2)

@when('I enter "{CarasSeverin}" in State field')
def step_impl(context, CarasSeverin):
    context.RegisterPage.enter_state(CarasSeverin)
    time.sleep(2)

@when('I enter "{Z320038}" in Zip Code field')
def step_impl(context, Z320038):
    context.RegisterPage.enter_zipcode(Z320038)
    time.sleep(2)

@when('I enter "{P0726165557}" in Phone field')
def step_impl(context, P0726165557):
    context.RegisterPage.enter_phone(P0726165557)
    time.sleep(2)

@when('I enter "{SSN1740827354807}" in SSN field')
def step_impl(context, SSN1740827354807):
    context.RegisterPage.enter_ssn(SSN1740827354807)
    time.sleep(2)

@when('I enter "{Razvan1199774420241}" in User field')
def step_impl(context, Razvan1199774420241):
    context.RegisterPage.enter_user(Razvan1199774420241)
    time.sleep(2)

@when('I enter "{P123456789}" in Passw field')
def step_impl(context, P123456789):
    context.RegisterPage.enter_passw(P123456789)
    time.sleep(2)

@when('I enter "{P123456789}" in Confirm field')
def step_impl(context, P123456789):
    context.RegisterPage.enter_confirm_pass(P123456789)
    time.sleep(2)

@when('I press the register1 button')
def steps_impl(context):
    context.RegisterPage.click_register_button()

@then('I should see an message')
def step_impl(context):
    actual_error_message = context.RegisterPage.get_message()
    expected_error_message = 'This username already exists.'
    assert expected_error_message in actual_error_message

```

## 📌 Am creat fisierul python browser.py

```
markdown
from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()
```

## 📌  Am creat fisierul python environment.py

```
markdown
from browser import Browser
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.RegisterPage = RegisterPage()

def after_all(context):
    context.browser.close()

```

## 📌 Am rulat testele cu comnda **behave -f html -o behave-reportR1.html** iar rezultatele au fost exportate intr-un fisier extern HTML 
    
  - Dupa rularea testelor pe meniul Register am raportat 12 teste passed si un test failed .
    
    ![image](https://github.com/razvanandrei1974/QA-Automation-Project-Parabank-website/assets/144438182/d2226e90-1fbf-4eca-bd2c-90b57af38a53)
    Testul failed este pentru afisarea mesajului dupa ce dam clik pe butonul Register.

  

## 📌 Concluzii -interpretare rezultate

Dupa rularea testelor trebuie raportat un bug care apare cand dam click pe butonul register.


