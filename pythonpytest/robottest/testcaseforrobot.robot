*** Settings ***
Library  Browser
Library  otp.py

*** Variables ***
${BROWSER}  chromium
${HEADLESS}  False

*** Test Cases ***
Login with MFA
    New Page   https://seleniumbase.io/realworld/login
    Fill Text    selector    txt
    Fill Text    id=username    demo_user
    Fill Text    id=password    secret_pass
    ${totp}  Get Totp  GAXG2MTEOR3DMMDG
    Fill Text    id=totpcode     ${totp}
    Click    "Sign in"
    Get Text  h1  ==  Welcome!