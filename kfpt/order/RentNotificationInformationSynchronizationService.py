#!/usr/bin/python
# -*- coding=utf-8 -*-

import threading
import requests
import chardet
import suds
import sys
sys.path.append('/root/git_20170730/kfpt')
import jiami
import config
import jiemi
reload(sys)
sys.setdefaultencoding('utf-8')

def DI7():
    print u">> T03-T-O-003 起租通知信息同步服务"
    print "*************"
    r_id = "1000198"
    token = "MTAwM2FiY1QwM19UT18wMDN4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T03_TO_003</SERVICE_CODE><ACCESS_TOKEN>"+ token +"</ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><REQUEST_ID>"+ r_id +"</REQUEST_ID><PROVINCE_CODE>340000</PROVINCE_CODE><REGION_CODE>340104</REGION_CODE><COUNTY_CODE>340501</COUNTY_CODE><CUST_COMPANY>1003</CUST_COMPANY><REGION_ID></REGION_ID><REGION_CODE></REGION_CODE><SITE_REGION></SITE_REGION><agreement_id></agreement_id><SITE_ID></SITE_ID><SITE_NAME></SITE_NAME><detail_address></detail_address><longitude></longitude><latitude></latitude><active_time></active_time><inactive_time></inactive_time><Shareinfo></Shareinfo><tower_type></tower_type><room_type></room_type><BATTERY></BATTERY><is_generation></is_generation><zero_six></zero_six><iselec></iselec><rent_list_power_mode></rent_list_power_mode><power_mode></power_mode><MAINTAIN></MAINTAIN><windFactor></windFactor><Unit1_count></Unit1_count><Unit1_HEIGHT></Unit1_HEIGHT><Unit1_antenna></Unit1_antenna><Unit1_system></Unit1_system><Unit1_bbu_sel></Unit1_bbu_sel><Unit1_rru_hang></Unit1_rru_hang><Unit1_bbu_fee></Unit1_bbu_fee><Unit2_count></Unit2_count><Unit2_HEIGHT></Unit2_HEIGHT><Unit2_antenna></Unit2_antenna><Unit2_system></Unit2_system><Unit2_bbu_sel></Unit2_bbu_sel><Unit2_rru_hang></Unit2_rru_hang><Unit2_bbu_fee></Unit2_bbu_fee><Unit3_count></Unit3_count><Unit3_HEIGHT></Unit3_HEIGHT><Unit3_antenna></Unit3_antenna><Unit3_system></Unit3_system><Unit3_bbu_sel></Unit3_bbu_sel><Unit3_rru_hang></Unit3_rru_hang><Unit3_bbu_fee></Unit3_bbu_fee><tower_share_count></tower_share_count><room_share_count></room_share_count><maint_share_count></maint_share_count><Rent_fee></Rent_fee><power_gen_share_cout></power_gen_share_cout><tower_pice_s></tower_pice_s><Room_pice_s></Room_pice_s><maint_fee></maint_fee><Rent_fee></Rent_fee><power_gen_fee></power_gen_fee><maint_discount></maint_discount><rent_discount></rent_discount><power_gen_discount></power_gen_discount><tower_discount></tower_discount><room_discount></room_discount><Is_rru_discount></Is_rru_discount><Power_fee></Power_fee><Oil_fee></Oil_fee><OVER_FEE></OVER_FEE><BATTERY_FEE></BATTERY_FEE><WLAN_FEE></WLAN_FEE><Micro_FEE></Micro_FEE><Other_fee></Other_fee><Other_fee_remark></Other_fee_remark><all_fee></all_fee><all_fee_tax></all_fee_tax><High_towe></High_towe><Nt_model></Nt_model><Power_charge_mode></Power_charge_mode></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    u = config.url + "/services/rentNotificationInformationSynchronization?wsdl"
    cc = suds.client.Client(u).service.RentNotificationInformationSynchronization(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    print ">> 返回报文:\n",jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__== "__main__":
    for i in range(1):
        for i in range(1):
            t = threading.Thread(target=DI7, args=())
            t.start()
        t.join()
    print ">> program run end"
