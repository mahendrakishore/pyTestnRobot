*** Settings ***
Documentation  This is my robot test case Settings
Library  OperatingSystem

*** Test Cases ***
TEST
  Count Files In Directory    c:
  Log    This is Test Cases