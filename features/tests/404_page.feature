# Created by garnikdadoyan at 2/27/21
Feature: test for 404 page
  # Enter feature description here

  Scenario: Amazon 404 page opens blog in another window
    Given Open Amazon Dress B0777K16R9V3 page
    When Store original windows
    And Click to open blog
    And Switch to newly opened window
    Then User can close new window and switch back to original window