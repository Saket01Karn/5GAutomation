import codecs
import shutil
import os
import sys

sys.path.insert(0, r'C:\Users\DELL\PycharmProjects\5GAutomation\VariableFiles')
import config_file


class HO:

    def __init__(self):
        pass

    def inter_ngran_ho_16(self):
        for i in range(1,17):
            print('UE = i',i)
            shutil.move(config_file.a1, config_file.b1)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\UE\UE1\meas_control.txt', "r", "utf-8") as f:
                if 'measconfig = measObject= 1' in f.read():
                    print("meas_control found")
                    #shutil.move(config_file.d1, config_file.c1)
                else:
                    print("meas_control not found")

            shutil.move(config_file.a2, config_file.b2)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\meas_report.txt', "r", "utf-8") as f:
                if 'PLMN ID = 40552' in f.read():
                    print("meas_report found")
                    #shutil.move(config_file.d2, config_file.c2)
                else:
                    print("meas_report not found")

            shutil.move(config_file.a3, config_file.b3)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg1.txt', "r", "utf-8") as f:
                if 'gNB configuration transfer' in f.read():
                    print("gNB configuration transfer found")
                    #shutil.move(config_file.d3, config_file.c3)
                else:
                    print("gNB configuration transfer not found")

            shutil.move(config_file.a4, config_file.b4)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\target_gNB\msg2.txt', "r", "utf-8") as f:
                if 'AMF Configuration Transfer' in f.read():
                    print("AMF Configuration Transfer found")
                    #shutil.move(config_file.d4, config_file.c4)
                else:
                    print("AMF Configuration Transfer not found")

            shutil.move(config_file.a5, config_file.b5)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg3.txt', "r", "utf-8") as f:
                if 'gNB configuration transfer' in f.read():
                    print("gNB configuration transfer found")
                    #shutil.move(config_file.d5, config_file.c5)
                else:
                    print("gNB configuration transfer not found")

            shutil.move(config_file.a6, config_file.b6)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\msg4.txt', "r", "utf-8") as f:
                if 'AMF configuration transfer' in f.read():
                    print("AMF configuration transfer found")
                    #shutil.move(config_file.d6, config_file.c6)
                else:
                    print("AMF configuration transfer not found")

            shutil.move(config_file.a7, config_file.b7)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\target_gNB\msg5.txt', "r", "utf-8") as f:
                if 'Xn setup request' in f.read():
                    print("Xn setup request found")
                    #shutil.move(config_file.d7, config_file.c7)
                else:
                    print("Xn setup request not found")

            shutil.move(config_file.a8, config_file.b8)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\msg6.txt', "r", "utf-8") as f:
                if 'Xn setup response' in f.read():
                    print("Xn setup response found")
                    #shutil.move(config_file.d8, config_file.c8)
                else:
                    print("Xn setup response not found")

            shutil.move(config_file.a9, config_file.b9)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\target_gNB\msg7.txt', "r", "utf-8") as f:
                if 'Handover Request' in f.read():
                    print("Handover Request found")
                # shutil.move(config_file.d9, config_file.c9)
                else:
                    print("Handover Request not found")
            # shutil.move(config_file.d9, config_file.c9)
            shutil.move(config_file.a10, config_file.b10)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\msg8.txt', "r", "utf-8") as f:
                if 'Handover Response Ack' in f.read():
                    print("Handover Response Ack found")
                    #shutil.move(config_file.d10, config_file.c10)
                else:
                    print("Handover Response Ack not found")

            shutil.move(config_file.a11, config_file.b11)
            with codecs.open(r'C:\Users\DELL\Desktop\loc\UE\UE1\msg9.txt', "r", "utf-8") as f:
                if 'RRC Reconfiguration' in f.read():
                    print("RRC Reconfiguration found")
                    #shutil.move(config_file.d11, config_file.c11)
                else:
                    print("RRC Reconfiguration not found")

            shutil.move(config_file.d1, config_file.c1)
            shutil.move(config_file.d2, config_file.c2)
            shutil.move(config_file.d3, config_file.c3)
            shutil.move(config_file.d4, config_file.c4)
            shutil.move(config_file.d5, config_file.c5)
            shutil.move(config_file.d6, config_file.c6)
            shutil.move(config_file.d7, config_file.c7)
            shutil.move(config_file.d8, config_file.c8)
            shutil.move(config_file.d9, config_file.c9)
            shutil.move(config_file.d10, config_file.c10)
            shutil.move(config_file.d11, config_file.c11)

    def inter_ngran_ho_32(self):
            for i in range(1,33):
                print('UE = i',i)
                shutil.move(config_file.a1, config_file.b1)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\UE\UE1\meas_control.txt', "r", "utf-8") as f:
                    if 'measconfig = measObject= 1' in f.read():
                        print("meas_control found")
                        #shutil.move(config_file.d1, config_file.c1)
                    else:
                        print("meas_control not found")

                shutil.move(config_file.a2, config_file.b2)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\meas_report.txt', "r", "utf-8") as f:
                    if 'PLMN ID = 40552' in f.read():
                        print("meas_report found")
                        #shutil.move(config_file.d2, config_file.c2)
                    else:
                        print("meas_report not found")

                shutil.move(config_file.a3, config_file.b3)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg1.txt', "r", "utf-8") as f:
                    if 'gNB configuration transfer' in f.read():
                        print("gNB configuration transfer found")
                        #shutil.move(config_file.d3, config_file.c3)
                    else:
                        print("gNB configuration transfer not found")

                shutil.move(config_file.a4, config_file.b4)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\target_gNB\msg2.txt', "r", "utf-8") as f:
                    if 'AMF Configuration Transfer' in f.read():
                        print("AMF Configuration Transfer found")
                        #shutil.move(config_file.d4, config_file.c4)
                    else:
                        print("AMF Configuration Transfer not found")

                shutil.move(config_file.a5, config_file.b5)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\5GC\AMF\msg3.txt', "r", "utf-8") as f:
                    if 'gNB configuration transfer' in f.read():
                        print("gNB configuration transfer found")
                        #shutil.move(config_file.d5, config_file.c5)
                    else:
                        print("gNB configuration transfer not found")

                shutil.move(config_file.a6, config_file.b6)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\msg4.txt', "r", "utf-8") as f:
                    if 'AMF configuration transfer' in f.read():
                        print("AMF configuration transfer found")
                        #shutil.move(config_file.d6, config_file.c6)
                    else:
                        print("AMF configuration transfer not found")

                shutil.move(config_file.a7, config_file.b7)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\target_gNB\msg5.txt', "r", "utf-8") as f:
                    if 'Xn setup request' in f.read():
                        print("Xn setup request found")
                        #shutil.move(config_file.d7, config_file.c7)
                    else:
                        print("Xn setup request not found")

                shutil.move(config_file.a8, config_file.b8)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\msg6.txt', "r", "utf-8") as f:
                    if 'Xn setup response' in f.read():
                        print("Xn setup response found")
                        #shutil.move(config_file.d8, config_file.c8)
                    else:
                        print("Xn setup response not found")

                shutil.move(config_file.a9, config_file.b9)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\target_gNB\msg7.txt', "r", "utf-8") as f:
                    if 'Handover Request' in f.read():
                        print("Handover Request found")
                    # shutil.move(config_file.d9, config_file.c9)
                    else:
                        print("Handover Request not found")
                # shutil.move(config_file.d9, config_file.c9)
                shutil.move(config_file.a10, config_file.b10)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\source_gNB\msg8.txt', "r", "utf-8") as f:
                    if 'Handover Response Ack' in f.read():
                        print("Handover Response Ack found")
                        #shutil.move(config_file.d10, config_file.c10)
                    else:
                        print("Handover Response Ack not found")

                shutil.move(config_file.a11, config_file.b11)
                with codecs.open(r'C:\Users\DELL\Desktop\loc\UE\UE1\msg9.txt', "r", "utf-8") as f:
                    if 'RRC Reconfiguration' in f.read():
                        print("RRC Reconfiguration found")
                        #shutil.move(config_file.d11, config_file.c11)
                    else:
                        print("RRC Reconfiguration not found")

                shutil.move(config_file.d1, config_file.c1)
                shutil.move(config_file.d2, config_file.c2)
                shutil.move(config_file.d3, config_file.c3)
                shutil.move(config_file.d4, config_file.c4)
                shutil.move(config_file.d5, config_file.c5)
                shutil.move(config_file.d6, config_file.c6)
                shutil.move(config_file.d7, config_file.c7)
                shutil.move(config_file.d8, config_file.c8)
                shutil.move(config_file.d9, config_file.c9)
                shutil.move(config_file.d10, config_file.c10)
                shutil.move(config_file.d11, config_file.c11)

    def gNB_HO(self):
        print('gNB asking UE to perform meas_control and send meas_report')
        print('gNB gets the meas_report ....\nfind the target cell')


        cellid1 = config_file.cell_id1
        cellid2 = config_file.cell_id2
        cellid = config_file.cell_id

        gnb_id1 = config_file.gNb_id11
        gnb_id2 = config_file.gNb_id22
        gnb_id = config_file.gNb_id1
        if gnb_id1 == gnb_id:
            print('Intra-Frequency HO happened')
            print(config_file.PCI)
            print(config_file.mcc, config_file.mnc)
            if cellid == cellid1 | cellid == cellid2:
                print('Intra-Freq Successful')
            else:
                print('gNb does not initiate HO')

        elif gnb_id2 == gnb_id:
            print('Inter-Freq HO Happened')
            print(config_file.PCI)
            print(config_file.mcc, config_file.mnc)
            if cellid == cellid1 | cellid == cellid2:
                print('Inter-Freq Successful')
                for i in range(0,255):
                    print('PLMN ID =',i)
            else:
                print('gNb does not initiate HO')

        else:
            print('HO will not initiate')

    def meas_config_27(self):
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'measObject to removal' in f.read():
                print("perform measObject to removal procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'measobject to addmodlist' in f.read():
                print("perform measobject to addmodlist")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'reportconfig to removal' in f.read():
                print("perform reportconfig to removal procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'reportconfig to addmodlist' in f.read():
                print("perform reportconfig to addmodlist procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'quantity config' in f.read():
                print("perform quantity config procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'measid to remove list' in f.read():
                print("perform measid to remove list procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'measid to addmodlist' in f.read():
                print("perform measid to addmodlist procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'measGap config' in f.read():
                print("perform measGap config procedure")
        with codecs.open(config_file.pth, "r", "utf-8") as f:
            if 'set RSRP, Varmeasconfig' in f.read():
                print("perform set RSRP, Varmeasconfig procedure")