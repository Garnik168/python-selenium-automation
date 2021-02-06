# Created by garnikdadoyan at 2/5/21
Feature: Adding items to the cart
  # Enter feature description here

  Scenario: Verify that new idem has been added to the cart
    Given Open Apple Mag Safe Charger page on Amazon
    When Click on Add to Cart button
    Then Check that confirmation pop-up is present
    When Click on Cart
    Then Verify that there is one item in the cart
