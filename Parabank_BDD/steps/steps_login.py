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

# @then('I should see an error for email')
# def step_impl(context):
#     actual_error_message = context.LoginPage.get_email_error()
#     expected_error_message = 'Wrong email'
#     assert expected_error_message in actual_error_message
