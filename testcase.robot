*** Settings ***
Library      os
Resource     ${EXEC_DIR}/Res/keyword.robot
Variables    ${EXEC_DIR}/VariableFiles/config_file.py
Library      ${EXEC_DIR}/Lib/Attach.py

*** Test Cases ***
Attach_test
    Unlocking
    Move
    Validate
    Cell_selection
    rrc_reject
    mo_sms1
    Locking1


*** Keywords ***

Move
    RACH_PREAMBLE
    L2_L3_MSG

Validate
    RACH_RESPONSE
    CONTENTION_RESOLUTION

Cell_selection
    selectedcell

Unlocking
    unlock

Locking1
    lock

rrc_reject
    RRC_REJECT1
    RRC_REJECT2

mo_sms1
    MO_SMS
