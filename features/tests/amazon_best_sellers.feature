# Created by garnikdadoyan at 2/12/21
Feature: Test Amazon Best Sellers
  # Enter feature description here

  Scenario: Verify that 5 bestseller links are present
    Given Open Amazon Best Sellers page
    Then Verify 5 Best Sellers links are present