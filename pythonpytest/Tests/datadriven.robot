*** Settings ***
Test Template    Login with invalid credentials should fail


*** Test Cases ***
Invalid User Name                 invalid          ${VALID PASSWORD}
Invalid Password                  ${VALID USER}    invalid
Invalid User Name and Password    invalid          invalid
Empty User Name                   ${EMPTY}         ${VALID PASSWORD}
Empty Password                    ${VALID USER}    ${EMPTY}
Empty User Name and Password      ${EMPTY}         ${EMPTY}


*** Keywords ***
Login with invalid credentials should fail
    [Arguments]    ${uname}    ${pass}
    Log Many   ${uname}    ${pass}