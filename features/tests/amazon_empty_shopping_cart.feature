# Created by garnikdadoyan at 2/5/21
Feature: Amazon shopping cart test
  # Enter feature description here

  Scenario: Verify that shopping cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Verify that Cart is Empty