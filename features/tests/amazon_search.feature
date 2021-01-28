# Created by garnikdadoyan at 1/26/21
Feature: Amazon Search Test
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Lightsaber into Amazon search field
    And Click on Amazon search icon
    Then Product results for Lightsaber are shown on Amazon