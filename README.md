# QA-Automation-Project-Parabank-website 🔄( Under Construction)

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
    ![image](https://github.com/razvanandrei1974/QA-Automation-Project-Parabank-website/assets/144438182/750a93a4-5681-443d-8594-c3c5a2825368)
    
  - Dupa rularea testelor pe meniul Register am raportat 12 teste passed si un test failed .
    ![image](https://github.com/razvanandrei1974/QA-Automation-Project-Parabank-website/assets/144438182/d2226e90-1fbf-4eca-bd2c-90b57af38a53)
    Testul failed este pentru afisarea mesajului dupa ce dam clik pe butonul Register.

  


## 📌 Concluzii -interpretare rezultate

Dupa rularea testelor 


