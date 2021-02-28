# Created by garnikdadoyan at 2/27/21
Feature: Amazon Terms and Conditions Test Amazon Applications
  # Enter feature description here

  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Verify that Amazon app page is opened
    And User can close new window and switch back to original
