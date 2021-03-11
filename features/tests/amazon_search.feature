# Created by garnikdadoyan at 1/26/21
Feature: Amazon Search Test
  # Enter feature description here

  Scenario Outline: User can search for a Lightsaber
    Given Open Amazon page
    When Input <search_query> into Amazon search field
    And Click on Amazon search icon
    Then Product results for <result> are shown on Amazon
    And Page URL address contains word <search_query>
    Examples:
    |search_query |result      |
    |Lightsaber   |"Lightsaber"|
    |Compass      |"Compass"   |

  Scenario: User can search for a Compass
    Given Open Amazon page
    When Input Compass into Amazon search field
    And Click on Amazon search icon
    Then Product results for "Compass" are shown on Amazon
    And Page URL address contains word Compass

  Scenario: User can add a product to the cart without any additional selections
    Given Open Amazon page
    When Search for coffee mug
    And Click on the first product
    And Click on Add to Cart button (Lana's version)
    Then Verify cart has 1 item

# # #
# Separated them with additional info in the Scenario name for separate running
# # #

  Scenario: User can add a product to the cart with additional selections (SIZE)
    Given Open Amazon page
    When Search for shoes
    And Click on the first product
    And Select item's size
    And Click on Add to Cart button (Lana's version)
    Then Verify cart has 1 item
