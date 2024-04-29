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




