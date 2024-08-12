# _**QA-Automation-Project-Parabank-website**_ 🔄

📍We created the automated test plan with Behave for the _"Login"_ menu , _"Register"_ menu abd _Open Account_ menu for
the Parabank application.

📍We used the Selenium library to automate the actions of navigation and interaction with the web interface.

## 📌 Installation and configuration:

🖥️ I installed Behave, , WebDriver for Python.

![Install Behave](https://github.com/user-attachments/assets/a8c9c207-793a-4bdc-8552-82071da59d66)

### pip install behave

🖥️ I installed Selenium Library

### pip install -U selenium

![Selenium](https://github.com/user-attachments/assets/21ebede8-3d86-49a0-9d0c-74ace9dbe3f1)
![Selenium Upgrade](https://github.com/user-attachments/assets/668da2f2-ed1d-49d0-b1b3-1f10a6c975dc)

🖥️ I installed WebDriver for Python

```ruby

from selenium.webdriver.common.by import By

from browser import Browser
```
![Requirements Files](https://github.com/user-attachments/assets/d9e1a35f-8902-426f-ad33-59dba4cd5920)

## Create _Pages_ directory which includes the following files :

### 📄 login.page

```ruby

from selenium.webdriver.common.by import By

from browser import Browser

class LoginPage(Browser):
USERNAME_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[1]/input')
PASSWORD_FIELD_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[2]/input')
LOGIN_BUTTON_SELECTOR = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input')
MESSAGE_ERROR_LABEL = (By.XPATH, '//*[@id="rightPanel"]/p')

    def navigate_to_login_page(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD_SELECTOR).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LABEL).text
```

### 📄register.page

```ruby
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
    USER_FIELD_SELECTOR = (By.XPATH, '//*[@id="customer.username"]')
    PASSW_FIELD_SELECTOR = (By.XPATH, '//*[@id="customer.password"]')
    CONFIRM_FIELD_SELECTOR = (By.XPATH, '//*[@id="repeatedPassword"]')
    SUBMIT_BUTTON_SELECTOR = (By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
    MESSAGE_ERROR_LABEL = (By.XPATH, '//*[@id="repeatedPassword.errors"]')

    def navigate_to_register_page(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

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

    def enter_user(self, Razvan11997744):
        self.driver.find_element(*self.USER_FIELD_SELECTOR).send_keys(Razvan11997744)

    def enter_passw(self, Bnc48757960):
        self.driver.find_element(*self.PASSW_FIELD_SELECTOR).send_keys(Bnc48757960)

    def enter_confirm_field(self, Bnc487579601):
        self.driver.find_element(*self.CONFIRM_FIELD_SELECTOR).send_keys(Bnc487579601)

    def click_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON_SELECTOR).click()

    def get_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LABEL).text
```

### 📄openaccount.page

``` ruby
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@given('I am on the open account page')
def step_given_on_open_account_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://parabank.parasoft.com/parabank/openaccount.htm')


@when('I fill in the account details')
def step_when_fill_in_account_details(context):
    # Select account type
    account_type_dropdown = Select(context.browser.find_element(By.ID, 'type'))
    account_type_dropdown.select_by_visible_text('SAVINGS')

    # Select from account
    from_account_dropdown = Select(context.browser.find_element(By.ID, 'fromAccountId'))
    from_account_dropdown.select_by_index(0)  # Select the first account in the list


@when('I submit the form')
def step_when_submit_form(context):
    submit_button = context.browser.find_element(By.XPATH, '//input[@value="Open New Account"]')
    submit_button.click()


@then('I should see a confirmation message')
def step_then_see_confirmation_message(context):
    confirmation_message = context.browser.find_element(By.XPATH, '//h1[text()="Account Opened!"]')
    assert confirmation_message.is_displayed()

```

## 💻Scenario outlines

Scenarios can be parametrized to cover multiple cases. These are called Scenario Outlines in Gherkin, and the variable
templates are written using angular brackets.

Example :

## ▶️ Definition of test scenarios:

1. Create _Features_ directory which includes the following files :

### 🟢login.features

▶️ Functionality Menu Login with real and corect data.

```ruby
  Feature: Login Feature
  Background:
    Given I am on the login page
  @first
  Scenario: Login with wrong credentials

    When I enter "Razvan1199774499@" in username field
    And I enter "Bnc48757960$" in password field
    And I press the login button
    Then I should see an error message
```

### 🟢 login1.features

▶️ Functionality Menu Login with unreal data.

```ruby
  Feature: Login Feature
  Background:
    Given I am on the login page
  @first
  Scenario: Login with wrong credentials

    When I enter "user_name" in username field
    And I enter "password" in password field
    And I press the login button
    Then I should see an error message
```

### 🟢 register.features

 ```ruby
Feature: Register Feature

  Background:
    Given I am on the register page

  @second
  Scenario: Register with corect and real credentials.

    # When I press the logout button
    When I press the register button
    And I enter "Razvan" in FirstName field
    And I enter "Ungar" in LastName field
    And I enter "Ciocarliei" in Adress field
    And I enter "Resita" in City field
    And I enter "CarasSeverin" in State field
    And I enter "Z320038" in Zip Code field
    And I enter "P0726165557" in Phone field
    And I enter "SSN1740827354807" in SSN field
    And I enter "Razvan11997744" in User field
    And I enter "Bnc48757960" in Passw field
    And I enter "Bnc487579601" in Confirm field
    And I press the submit button
    Then I should see an error register message
```

### 🟢 openaccount.features

```ruby
Feature: Open account

#  Background:
#  As a user
#  I want to open a new account
#  So that I can use the banking services
  @three
  Scenario: Successfully open a new account
    Given I am on the open account page
    When I fill in the account details
    And I submit the form
    Then I should see a confirmation message
```

## 💻Test setup

Test setup is implemented within the Given section. Even though these steps are executed imperatively to apply possible
side-effects, pytest-bdd is trying to benefit of the PyTest fixtures which is based on the dependency injection and
makes the setup more declarative style.

Many other BDD toolkits operate on a global context and put the side effects there. This makes it very difficult to
implement the steps, because the dependencies appear only as the side-effects during run-time and not declared in the
code. The "publish article" step has to trust that the article is already in the context, has to know the name of the
attribute it is stored there, the type etc.

In pytest-bdd you just declare an argument of the step function that it depends on and the PyTest will make sure to
provide it.

Still side effects can be applied in the imperative style by design of the BDD.

Example :

##  Create _Steps_ directory which includes the following files :

### 🔀 steps.login

``` ruby
import time

from behave import *


@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()


@when('I enter "{username}" in username field')
def step_impl(context, username):
    context.LoginPage.enter_username(username)
    time.sleep(3)


@when('I enter "{password}" in password field')
def step_impl(context, password):
    context.LoginPage.enter_password(password)


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_error_message = 'The username and password could not be verified.'
    assert expected_error_message in actual_error_message


@when('I press the login button')
def steps_impl(context):
    context.LoginPage.click_login_button()

# @then('I should see an error for email')
# def step_impl(context):
#     actual_error_message = context.LoginPage.get_email_error()
#     expected_error_message = 'Wrong email'
#     assert expected_error_message in actual_error_message
```

### 🔀 steps.register

``` ruby

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
    time.sleep(1)


@when('I enter "{Caras_Severin}" in State field')
def step_impl(context, Caras_Severin):
    context.RegisterPage.enter_state(Caras_Severin)
    time.sleep(1)


@when('I enter "{Z320038}" in Zip Code field')
def step_impl(context, Z320038):
    context.RegisterPage.enter_zipcode(Z320038)
    time.sleep(1)


@when('I enter "{P0726165557}" in Phone field')
def step_impl(context, P0726165557):
    context.RegisterPage.enter_phone(P0726165557)
    time.sleep(1)


@when('I enter "{SSN1740827354807}" in SSN field')
def step_impl(context, SSN1740827354807):
    context.RegisterPage.enter_ssn(SSN1740827354807)
    time.sleep(1)


@when('I enter "{Razvan1199774499}" in User field')
def step_impl(context, Razvan1199774499):
    context.RegisterPage.enter_user(Razvan1199774499)
    time.sleep(1)


@when('I enter "{Bnc48757960}" in Passw field')
def step_impl(context, Bnc48757960):
    context.RegisterPage.enter_passw(Bnc48757960)
    time.sleep(1)


@when('I enter "{Bnc487579601}" in Confirm field')
def step_impl(context, Bnc487579601):
    context.RegisterPage.enter_confirm_field(Bnc487579601)
    time.sleep(1)


@when('I press the submit button')
def steps_impl(context):
    context.RegisterPage.click_submit_button()


@then('I should see an error register message')
def step_impl(context):
    actual_error_message = context.RegisterPage.get_message()
    expected_error_message = 'Passwords did not match.'
    assert expected_error_message in actual_error_message
```

### 🔀 steps.openaccount

``` ruby

from behave import given, when, then
from selenium import webdriver


@given('I am on the open account page')
def step_given_on_open_account_page(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://parabank.parasoft.com/parabank/openaccount.htm')


@when('I fill in the account details')
def step_when_fill_in_account_details(context):
    # Add code to fill in the form details
    pass


@when('I submit the form')
def step_when_submit_form(context):
    # Add code to submit the form
    pass


@then('I should see a confirmation message')
def step_then_see_confirmation_message(context):
    # Add code to verify the confirmation message
    pass
```

## 💻Hooks

pytest-bdd exposes several pytest hooks which might be helpful building useful reporting, visualization, etc. on top of
it:

* pytest_bdd_before_scenario(login, register, openaccount) - Called before scenario is executed

- pytest_bdd_after_scenario(login, register, openaccount) - Called after scenario is executed (even if one of steps has
  failed)

+ pytest_bdd_login_step(login, feature, step, step_func) - Called before step function is executed and it's arguments
  evaluated

* pytest_bdd_register_step(register, feature, step, step_func) - Called before step function is executed and it's
  arguments evaluated

- pytest_bdd_openaccount_step(openaccount, feature, step, step_func) - Called before step function is executed and it's
  arguments evaluated

## Reporting

### We executed the tests with the order

behave -f html -o behave-report2000.html

![BEHAVE TEST REPORT](https://github.com/user-attachments/assets/10fab3fb-62a5-457d-af77-38afe0dd4406)























