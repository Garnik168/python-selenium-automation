# Created by garnikdadoyan at 3/20/21
Feature: New Arrivals feature
  # Enter feature description here

  Scenario: User sees New Arrival deals while hovering over New Arrivals on product page
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify User sees New Arrival flyout