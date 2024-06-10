Feature: Test Scenario for clicking on the left side of the main page

  @smoke
  Scenario: The user can click on “Connect the company” on the left side of the main page
    Given Open the main page
    When Log in to the page
    And Click on “Connect the company”
    And Switch to the new tab
    Then Verify the right tab opens