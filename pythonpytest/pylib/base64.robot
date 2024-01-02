*** Settings ***
Library    base64py.py


*** Test Cases ***
Use Custom
    ${base64}    Encoding    This is a Test String
    Log   ${base64}
    ${decode}    Decoding    ${base64}
    Log    ${decode}