# Created by garnikdadoyan at 2/16/21
Feature: Amazon Sign In Test
  # Enter feature description here

  Scenario: Sign in page can be open from sign in pop-up
    Given Open Amazon page
    When Click Sign In from pop-up
    Then Verify Sign In page opens