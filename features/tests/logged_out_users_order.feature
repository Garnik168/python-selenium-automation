# Created by garnikdadoyan at 1/27/21
Feature: Logged out user order
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon main page
    Then Click on Orders
    And User is taken to Sign in page