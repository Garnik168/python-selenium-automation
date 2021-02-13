# Created by garnikdadoyan at 2/12/21
Feature: Adding and deleting items Amazon cart TEST
  # Enter feature description here

  Scenario: Verify that item was successfully added to the cart and deleted from the cart
    Given Open Amazon page
    When Input Macbook Pro M1 into Amazon search field and hit ENTER
    And Click on the first unsponsored result
    When Click on Add to Cart button
    And Choose No Thanks option for Add ons
    Then Verify that alert Added to Cart is present
    When Click on Cart button on the pop-up screen
    Then Verify that there is one item in the cart
    When Click on Delete button under item in the cart
    Then Verify that Cart is Empty

# While I was enhancing it I though, why not to add one more option like deleting items from the cart :)