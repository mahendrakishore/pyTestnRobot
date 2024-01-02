*** Variables ***
${novalue}    13/5



*** Test Cases ***
Test Case
    #Wait Until Keyword Succeeds    retry    retry_interval    name
    Wait Until Keyword Succeeds    2 min    5 sec    My keyword1    ${novalue}
    ${result}    Wait Until Keyword Succeeds    3x    200ms    My keyword
    ${result}    Wait Until Keyword Succeeds    3x    strict: 200ms    My keyword

*** Keywords ***
My keyword
   Log   My keyword
My keyword1
   [Arguments]  ${val}
   Log  ${val}