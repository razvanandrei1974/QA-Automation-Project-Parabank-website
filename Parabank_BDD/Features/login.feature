Feature: Login Feature

  Background:
    Given I am on the login page

  @first
  Scenario: Login with wrong credentials

    When I enter "jhon1234" in username field
    And I enter "demo" in password field
    And I press the login button
    Then I should see an error message

#