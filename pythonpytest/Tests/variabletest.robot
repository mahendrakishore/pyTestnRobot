*** Test Cases ***

Test Case 1
    ${my_local_var}    Set Variable    Hello World
    Log    ${my_local_var}
    Set Suite Variable    ${my_suite_var}    I'm a suite variable
    Set Global Variable    ${my_global_var}    I'm a global variable

Test Case 2
    Log    ${my_local_var}

Test Case 3
    Test Keyword for Variables
    Log    ${my_keyword_var}
    Log    ${my_test_var}

*** Keywords ***
Test Keyword for Variables
   ${my_keyword_var}    Set Variable    Hello Keyword
   Log    ${my_keyword_var}
   Set Test Variable    ${my_test_var}    I'm a test case variable
