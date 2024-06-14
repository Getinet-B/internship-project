Feature: Test Scenario for clicking on the left side of the main page

  Scenario: The user can click on “Connect the company” button
    Given Open the main page
    When Log in to the page
    And Click on "Menu" on mobile app
    And Click on “Connect the company”
    And Switch to the new tab
    Then Verify the right tab opens