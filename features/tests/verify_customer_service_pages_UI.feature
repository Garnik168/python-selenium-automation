# Created by garnikdadoyan at 2/13/21
Feature: Verify that all required UI elements are present on the page
  # Enter feature description here

  Scenario: Verify Hello. What can we help you with? line is present
    Given Open Amazon Customer Service Help page
    Then Verify that Hello. What can we help you with line is present

  Scenario: Verify Some things you can do here section
    Given Open Amazon Customer Service Help page
    Then Verify that Some things you can do here section is present
    Then Verify that Some things you can do here section contains 8 self service rich cards

  Scenario: Verify Search Help Library and it's input field are present
    Given Open Amazon Customer Service Help page
    Then Verify that Search Help Library section is present
    Then Verify that Search Help Library input field is present

  Scenario: Verify Browse Help Topics Section
    Given Open Amazon Customer Service Help page
    Then Verify that Browse Help Topics section is present
    Then Verify that Browse Help Topics section contains 12 help getaway links

  Scenario: Verify image is present
    # Should I specify which img is present? like double check for which topic is active and check if it has a correct corresponding img?
    # In this case I think only verification of the img it self has to be checked, so I will not double check that Recommended Topics is active and that corresponding Wrenches image is present at this time
    Given Open Amazon Customer Service Help page
    Then Verify that image is present in Browse Help Topics
