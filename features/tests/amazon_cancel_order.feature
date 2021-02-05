# Created by garnikdadoyan at 2/4/21
Feature: Amazon Cancel Order Test
  # Enter feature description here

  Scenario: User has Cancel Item and Orders option available
    Given Open Amazon Help page
    When Input "Cancel order" into the help search field
    And Hit Enter button in the help search field
    Then Verify that 'Cancel Items or Orders' text is present