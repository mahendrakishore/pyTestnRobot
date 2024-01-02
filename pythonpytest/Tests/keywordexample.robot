*** Variables ***
${uname}  MahendraKishore

@{list}  list1  list2  list3

&{dictvar}  usrnm=mahendra  pass=kishore

*** Keywords ***
Login Test
  [Arguments]  ${username}
  Log  ${username}

Login Pass
   [Arguments]  ${password}
   Log  ${password}

Login uname and pass
  [Arguments]   ${username}  ${password}
  Login Test    ${username}
  Login Pass    ${password}


*** Test Cases ***
TEST
  [Tags]  keywordtest
  Login uname and pass  ${dictvar}[usrnm]  ${dictvar}[pass]

TEST2
  [Tags]  keywordtest
  FOR    ${ele}    IN    @{list}
      Log    ${ele}
  END
  FOR    ${key}  ${val}    IN    &{dictvar}
      Log Many   ${key}  ${val}
  END




