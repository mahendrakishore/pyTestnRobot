*** Test Cases ***
Login With Admin
    Given I am on the login page
    When I login with username "admin" and password "admin"
    Then I should see the welcome page

Login With Invalid User
    Given I am on the login page
    When I login with username "invalid" and password "invalid"
    Then I should see the error message
    And I should be able to login again