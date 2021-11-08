# Paths for cell registration
source1 = r"C:\Users\DELL\Desktop\Locker\UE\Reg_Req.txt"
#des1 = destination = r"C:\Users\DELL\Desktop\Locker\gNb"

source2 = r"C:\Users\DELL\Desktop\Locker\gNb\Reg_Req.txt"
des2 = r"C:\Users\DELL\Desktop\Locker\5GC\New AMF\rxd"

source3 =r"C:\Users\DELL\Desktop\Locker\5GC\New AMF\ue_context_transfer.txt"
des3 = r"C:\Users\DELL\Desktop\Locker\5GC\Old AMF"

source4 =r"C:\Users\DELL\Desktop\Locker\5GC\Old AMF\ue_context_response.txt"
des4 =  r"C:\Users\DELL\Desktop\Locker\5GC\New AMF\rxd"

source5 =r"C:\Users\DELL\Desktop\Locker\5GC\New AMF\ID_Req.txt"
#des5 = d= r"C:\Users\DELL\Desktop\Locker\UE"

source6 = r"C:\Users\DELL\Desktop\Locker\UE\ID_Response.txt"
#des6 = des4 = r"C:\Users\DELL\Desktop\Locker\5GC\New AMF\rxd"

source7 = r"C:\Users\DELL\Desktop\Locker\5GC\New AMF\ausf_req.txt"
des7 = r"C:\Users\DELL\Desktop\Locker\5GC\AUSF"

source8 = r"C:\Users\DELL\Desktop\Locker\5GC\AUSF\udm_req.txt"
des8 =r"C:\Users\DELL\Desktop\Locker\5GC\UDM"

source9 = r"C:\Users\DELL\Desktop\Locker\5GC\UDM\udm_response.txt"
des9 = r"C:\Users\DELL\Desktop\Locker\5GC\AUSF"

source10 = r"C:\Users\DELL\Desktop\Locker\5GC\AUSF\ausf_response.txt"





#Paths for RACH
source = r"C:\Users\DELL\Desktop\Locker\UE\request_1.txt"
destination = r"C:\Users\DELL\Desktop\Locker\gNb"

s = r"C:\Users\DELL\Desktop\Locker\gNb\response_1.txt"
d = r"C:\Users\DELL\Desktop\Locker\UE"

s1 = r"C:\Users\DELL\Desktop\Locker\UE\request_2.txt"
#d1 = r"C:\Users\DELL\Desktop\Locker\gNb"

s2 = r"C:\Users\DELL\Desktop\Locker\gNb\response_2.txt"
#d2 = r"C:\Users\DELL\Desktop\Locker\UE"

gNb_req1 = r'C:\Users\DELL\Desktop\Locker\gNb\request_1.txt', "r", "utf-8"
gnb_req2 = r'C:\Users\DELL\Desktop\Locker\gNb\request_2.txt', "r", "utf-8"

ue_res1 = r'C:\Users\DELL\Desktop\Locker\UE\response_1.txt', "r", "utf-8"
ue_res2 = r'C:\Users\DELL\Desktop\Locker\UE\response_2.txt', "r", "utf-8"

pw = 'Saket@123'
#pw1 = input('Enter the password to unlock')
#pw2 = input('Enter the password to lock')


dir_path = r"C:\Users\DELL\Desktop"
loc_path = "Locker"

# Cell Selection and Reselection

#q_rxlevmeas = int(input('Enter RSRP VALUE in dBm'))
q_rxlevmin = -110 #dBm
q_rxlevminoffset = 0
P_max = 23

#q_qlevmeas = int(input('Enter RSRQ VALUE in dBm'))
q_qlevmin = -3  # dBm
q_qlevminoffset = 0


#q_rxlevmeas2 = int(input('Enter RSRP VALUE in dBm'))
q_rxlevmin2 = -110 #dBm
q_rxlevminoffset2 = 0

#q_qlevmeas2 = int(input('Enter RSRQ VALUE in dBm'))
q_qlevmin2 = -3 # dBm
q_qlevminoffset2 = 0

#paths for RRC Reject

path1=r"C:\Users\DELL\Desktop\Locker\UE\pdu_session_req.txt"
path2=r"C:\Users\DELL\Desktop\Locker\5GC\SMF"

#paths for MO_SMS

p1 =r'C:\Users\DELL\Desktop\Locker\UE\msg1.txt'
p2 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF'
p3 =r'C:\Users\DELL\Desktop\Locker\UE\msg2.txt'
p4 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF'
p5 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg3.txt'
p6 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSF'
p7 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSF\msg4.txt'
p8 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSIWMSC'
p9 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSIWMSC\msg5.txt'
p10 =r'C:\Users\DELL\Desktop\Locker\5GC\SC'
p11 =r'C:\Users\DELL\Desktop\Locker\5GC\SC\msg5_frm_sc.txt'
p12 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSIWMSC'
p13 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSF\msg6.txt'
p14 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF'
p15 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg7.txt'
p16 =r'C:\Users\DELL\Desktop\Locker\UE'
p17 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSIWMSC\msg8.txt'
p18 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSF'
p19 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSF\msg9.txt'
p20 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF'
p21 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg10.txt'
p22 =r'C:\Users\DELL\Desktop\Locker\UE'
p23 =r'C:\Users\DELL\Desktop\Locker\UE\msg11.txt'
p24 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF'
p25 =r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg12.txt'
p26 =r'C:\Users\DELL\Desktop\Locker\5GC\SMSF'

####################################### HANDOVER PATHS #########################################

## paths for Xn based inter NGRAN handover ##

a1 =r'C:\Users\DELL\Desktop\loc\source_gNB\meas_control.txt'
b1 =r'C:\Users\DELL\Desktop\loc\UE\UE1'
a2 =r'C:\Users\DELL\Desktop\loc\UE\UE1\meas_report.txt'
b2 =r'C:\Users\DELL\Desktop\loc\source_gNB'
a3 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg1.txt'
b3 =r'C:\Users\DELL\Desktop\loc\5GC\AMF'
a4 =r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg2.txt'
b4 =r'C:\Users\DELL\Desktop\loc\target_gNB'
a5 =r'C:\Users\DELL\Desktop\loc\target_gNB\msg3.txt'
b5 =r'C:\Users\DELL\Desktop\loc\5GC\AMF'
a6 =r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg4.txt'
b6 =r'C:\Users\DELL\Desktop\loc\source_gNB'
a7 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg5.txt'
b7 =r'C:\Users\DELL\Desktop\loc\target_gNB'
a8 =r'C:\Users\DELL\Desktop\loc\target_gNB\msg6.txt'
b8 =r'C:\Users\DELL\Desktop\loc\source_gNB'
a9 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg7.txt'
b9 =r'C:\Users\DELL\Desktop\loc\target_gNB'
a10 =r'C:\Users\DELL\Desktop\loc\target_gNB\msg8.txt'
b10 =r'C:\Users\DELL\Desktop\loc\source_gNB'
a11 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg9.txt'
b11 =r'C:\Users\DELL\Desktop\loc\UE\UE1'

c1 =r'C:\Users\DELL\Desktop\loc\source_gNB'
d1 =r'C:\Users\DELL\Desktop\loc\UE\UE1\meas_control.txt'
c2 =r'C:\Users\DELL\Desktop\loc\UE\UE1'
d2 =r'C:\Users\DELL\Desktop\loc\source_gNB\meas_report.txt'
c3 =r'C:\Users\DELL\Desktop\loc\source_gNB'
d3 =r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg1.txt'
c4 =r'C:\Users\DELL\Desktop\loc\5GC\AMF'
d4 =r'C:\Users\DELL\Desktop\loc\target_gNB\msg2.txt'
c5 =r'C:\Users\DELL\Desktop\loc\target_gNB'
d5 =r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg3.txt'
c6 =r'C:\Users\DELL\Desktop\loc\5GC\AMF'
d6 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg4.txt'
c7 =r'C:\Users\DELL\Desktop\loc\source_gNB'
d7 =r'C:\Users\DELL\Desktop\loc\target_gNB\msg5.txt'
c8 =r'C:\Users\DELL\Desktop\loc\target_gNB'
d8 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg6.txt'
c9 =r'C:\Users\DELL\Desktop\loc\source_gNB'
d9 =r'C:\Users\DELL\Desktop\loc\target_gNB\msg7.txt'
c10 =r'C:\Users\DELL\Desktop\loc\target_gNB'
d10 =r'C:\Users\DELL\Desktop\loc\source_gNB\msg8.txt'
c11 =r'C:\Users\DELL\Desktop\loc\source_gNB'
d11 =r'C:\Users\DELL\Desktop\loc\UE\UE1\msg9.txt'

## Cell 1 details
mcc = input('val in range 0 to 7')
mnc = input('val in range 0 to 7')

PSS = input('enter value between 0 and 2')
SSS = input('enter value between 0 and 335')
PCI = 3*SSS + PSS

gNb_id11 = 500
gNb_id22 = 600

gNb_id1 = input('gnb_id 500 or 600')

cell_id1 = 15
cell_id2 = 5

cell_id = print('give val 5,15 & 10')

## path for 1.27 handover testcase########

pth = r'C:\Users\DELL\Desktop\loc\UE\UE1\Meas_Config.txt'