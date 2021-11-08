*** Settings ***
Library      os
Resource     ${EXEC_DIR}/Res/ho_keyword.robot
Variables    ${EXEC_DIR}/VariableFiles/config_file.py
Library      ${EXEC_DIR}/Lib/HO.py

*** Test Cases ***
inter_ngran_test
    ngran_ho1

*** Keywords ***

ngran_ho1
    inter_ngran_ho_16
    inter_ngran_ho_32
    gNB_HO
    meas_config_27