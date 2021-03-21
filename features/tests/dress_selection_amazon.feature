# Created by garnikdadoyan at 2/18/21
Feature: Test for dress selection
  # Enter feature description here

  Scenario: User can select dress colors
    Given Open Amazon Dress B07K16R9V3 page
    Then Verify user can click through colors
    
  Scenario: Size tooltip is shown upon hovering over Add To Cart button
    Given Open Amazon product B074TBCSC8 page
    When Hover over Add to Cart button
    Then Verify size selection tooltip is shown
