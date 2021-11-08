import codecs
import shutil
import os
import sys

sys.path.insert(0, r'C:\Users\DELL\PycharmProjects\5GAutomation\VariableFiles')
import config_file

#sys.path.append("../ExternalFile")



class Attach:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        pass


    def RACH_PREAMBLE(self):
        shutil.move(config_file.source, config_file.destination)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\gNb\request_1.txt', "r", "utf-8") as f:
            if 'Msg1' in f.read():
                print("Msg1 found")
            else:
                print("Msg1 not found")
    def RACH_RESPONSE(self):
        shutil.move(config_file.s, config_file.d)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\UE\response_1.txt', "r", "utf-8") as f1:
            if 'Msg2' in f1.read():
                print("Msg2 found")
            else:
                print("Msg2 not found")

    def L2_L3_MSG(self):
        shutil.move(config_file.s1, config_file.d1)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\gNb\request_2.txt', "r", "utf-8") as f2:
            if 'Msg3' in f2.read():
                print("Msg3 found")
            else:
                print("Msg3 not found")

    def CONTENTION_RESOLUTION(self):
        shutil.move(config_file.s2, config_file.d2)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\UE\response_2.txt', "r","utf-8") as f3:
            if 'Msg4' in f3.read():
                print("Msg4 found")

            else:
                print("Msg4 not found")



    def selectedcell(self):
        S_rxlev1 = config_file.q_rxlevmeas - (config_file.q_rxlevmin + config_file.q_rxlevminoffset) - config_file.P_max

        S_qlev1 = config_file.q_qlevmeas - (config_file.q_qlevmin + config_file.q_qlevminoffset)
        S_rxlev2 = config_file.q_rxlevmeas2 - (
                    config_file.q_rxlevmin2 + config_file.q_rxlevminoffset2) - config_file.P_max

        S_qlev2 = config_file.q_qlevmeas2 - (config_file.q_qlevmin2 + config_file.q_qlevminoffset2)

        if S_rxlev1 < S_rxlev2:
            if S_qlev1 < S_qlev2:
                if S_rxlev2>0 & S_qlev2>0:
                    print('Cell 2 is selected')
                else:
                    print('Cell 2 is not selected')
            else:
                print('Need for cell reselection')
        elif S_rxlev1 > S_rxlev2:
            if S_qlev1 > S_qlev2:
                if S_rxlev1>0 & S_qlev1>0:
                    print('Cell 1 is selected')
                else:
                    print('Cell 1 is not selected')
            else:
                print('Need for cell reselection')
        else:
            print('No cell selected')

    def RRC_REJECT1(self):
        print('Check for UE '
              '\n Configuration is successful')
        print('RACH DONE')
        print('Registration is successful')
        shutil.move(config_file.path1, config_file.path2)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SMF\pdu_session_req.txt', "r", "utf-8") as f:
            if 'UL NAS transport' in f.read():
                print("UL NAS transport found")
                print("PDU Session created")
                with codecs.open(r'C:\Users\DELL\Desktop\Locker\gNb\DU1\DU_OAM.txt', "r", "utf-8") as f1:
                    if 'MAXIMUM UE CAPACITY = FULL' in f1.read():
                        print('RRC REJECTED')
                with codecs.open(r'C:\Users\DELL\Desktop\Locker\gNb\DU2\DU_OAM.txt', "r", "utf-8") as f2:
                    if 'MAXIMUM UE CAPACITY = FULL' in f2.read():
                        print('RRC REJECTED')

            else:
                print("UL NAS transport not found")

    def RRC_REJECT2(self):
        print('Check for UE '
              '\n Configuration is successful')
        print('RACH DONE')
        print('Registration is successful')
        print("UL NAS transport found")
        print("PDU Session created")
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\gNb\CU\CU_OAM.txt', "r", "utf-8") as f1:
            if 'MAXIMUM DU CAPACITY = FULL' in f1.read():
                print('RRC REJECTED')

    def MO_SMS(self):
        shutil.move(config_file.p1, config_file.p2)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg1.txt', "r", "utf-8") as f:
            if 'UE Triggered Service Request' in f.read():
                print("UE Triggered Service Request found")
            else:
                print("UE Triggered Service Request not found")
        shutil.move(config_file.p3, config_file.p4)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg2.txt', "r", "utf-8") as f:
            if 'Uplink NAS Transport(SMS BPODY)' in f.read():
                print("Uplink NAS Transport(SMS BPODY) found")
            else:
                print("Uplink NAS Transport(SMS BPODY) not found")
        shutil.move(config_file.p5, config_file.p6)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SMSF\msg3.txt', "r", "utf-8") as f:
            if 'Nsmsf_SMService_UplinkSM' in f.read():
                print("Nsmsf_SMService_UplinkSM found")
            else:
                print("Nsmsf_SMService_UplinkSM not found")
        shutil.move(config_file.p7, config_file.p8)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SMSIWMSC\msg4.txt', "r", "utf-8") as f:
            if 'Forward MO' in f.read():
                print("Forward MO found")
            else:
                print("Forward MO not found")
        shutil.move(config_file.p9, config_file.p10)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SC\msg5.txt', "r", "utf-8") as f:
            if 'Msg xter' in f.read():
                print("Msg xter found")
            else:
                print("Msg xter not found")
        shutil.move(config_file.p11, config_file.p12)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SMSIWMSC\msg5_frm_sc.txt', "r", "utf-8") as f:
            if 'Msg rpt' in f.read():
                print("Msg rpt found")
            else:
                print("Msg rpt not found")
        shutil.move(config_file.p13, config_file.p14)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg6.txt', "r", "utf-8") as f:
            if 'Namf_Communication_N1N2MessageTransfer' in f.read():
                print("Namf_Communication_N1N2MessageTransfer found")
            else:
                print("Namf_Communication_N1N2MessageTransfer not found")
        shutil.move(config_file.p15, config_file.p16)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\UE\msg7.txt', "r", "utf-8") as f:
            if 'Downlink NAS Transport' in f.read():
                print("Downlink NAS Transport found")
            else:
                print("Downlink NAS Transport not found")
        shutil.move(config_file.p17, config_file.p18)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SMSF\msg8.txt', "r", "utf-8") as f:
            if 'Submit Report' in f.read():
                print("Submit Report found")
            else:
                print("Submit Report not found")
        shutil.move(config_file.p19, config_file.p20)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg9.txt', "r", "utf-8") as f:
            if 'Namf_Communication_N1N2MessageTransfer' in f.read():
                print("Namf_Communication_N1N2MessageTransfer found")
            else:
                print("Namf_Communication_N1N2MessageTransfer not found")
        shutil.move(config_file.p21, config_file.p22)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\UE\msg10.txt', "r", "utf-8") as f:
            if 'Downlink NAS Transport' in f.read():
                print("Downlink NAS Transport found")
            else:
                print("Downlink NAS Transport not found")
        shutil.move(config_file.p23, config_file.p24)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\New AMF\msg11.txt', "r", "utf-8") as f:
            if 'Msg1' in f.read():
                print("Msg1 found")
            else:
                print("Msg1 not found")
        shutil.move(config_file.p25, config_file.p26)
        with codecs.open(r'C:\Users\DELL\Desktop\Locker\5GC\SMSF\msg12.txt', "r", "utf-8") as f:
            if 'Nsmsf_SMService_UplinkSMS' in f.read():
                print("Nsmsf_SMService_UplinkSMS found")
            else:
                print("Nsmsf_SMService_UplinkSMS not found")

    def unlock(self):

        # Unlock the folder
        pw = config_file.pw

        # while True:
        pw1 = config_file.pw1
        if pw1 == pw:
            os.chdir(config_file.dir_path)
            if not os.path.exists(config_file.loc_path):
                if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                    os.mkdir("Locker")
                    print("Locker Folder Successfully created")

                else:
                    os.popen('attrib -h -s -r Locker')
                    os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                    print("Locker Folder has been Successfully Unlocked")
                    # break

            else:
                print("Locker folder is not LOCKED")

        else:
            print("wrong password! Try again later")

    def lock(self):  # lock the folder

        p_w = config_file.pw

        # while True:
        pw2 = config_file.pw2
        if pw2 == p_w:
            os.chdir(config_file.dir_path)
            # print("Your path Successfully Changed")
            # If Locker folder or Recycle bin does not exist then we will be create Locker Folder

            if os.path.exists(config_file.loc_path):
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # sys.exit()
                # break

            else:
                os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # break

        else:
            print("wrong password! Try again later")

        # break
