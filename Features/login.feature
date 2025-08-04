Feature: Login Functionality

  Scenario: BDD Valid login with correct username and password
    Given the user launches the application
    When the user enters valid credentials
    Then the user should land on the homepage
