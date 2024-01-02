*** Comments ***
Global variables use upper-case letters.
Suite variables use upper-case letters.
Test variables use upper-case letters.
Local variables use lower-case letters.
Keyword arguments use lower-case letters.


#*** Settings ***
Documentation
Metadata
Library
Resource
Variables
Suite Setup
Suite Teardown


#*** Variables ***
${VARIABLE}  This is a Variable
${COMPOSITE VARIABLES}  ${VARIABLE} with other variables.


#*** Test Cases ***  #*** Tasks ***

    [Documentation]
    [Tags]
    [Setup]
    [Template]
    [Timeout]
    #Static Variable Assignments
    #Keyword Calls
    #Verification Keyword Call
    [Teardown]


*** Keywords ***
    [Documentation]
    [Tags]
    [Arguments]
    [Timeout]
    #Static Variable Assignments
    #Keyword Calls
    [Teardown]

Keyword With Static Variables
    [Arguments]    ${argument}
    ${static variable}             Set Variable               This is a static variable.
    Set Local Variable             ${other static variable}   Another way to set a static variable.
    ${dynamic variable}            Catenate                   SEPARATOR=${SPACE}    ${static variable}                             ${other static variable}    ${argument}
    ${another dynamic variable}    Evaluate                   $static variable.upper()
    Log To Console                 ${dynamic variable}
    Should Not Be Equal            ${static variable}         ${other static variable}

