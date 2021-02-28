# Created by garnikdadoyan at 2/16/21
Feature: Amazon Sign In Test
  # Enter feature description here

  Scenario: Sign in page can be open from sign in pop-up
    Given Open Amazon page
    When Click Sign In from pop-up
    Then Verify Sign In page opens

  Scenario: Amazon users see sigh in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 8 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears
