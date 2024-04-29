Feature: Register Feature

  Background:
    Given I am on the register page

  @second
  Scenario: Register with corect credentials

#    When I press the logout button
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


