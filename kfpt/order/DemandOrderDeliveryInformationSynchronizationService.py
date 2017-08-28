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

def DI5():
    print u">> 需求订单交付验收信息同步服务"
    r_id = "1217080700015228"
    token = "MTAwM2FiY1QwM19UT18wMDJ4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T03_TO_002</SERVICE_CODE><ACCESS_TOKEN>"+ token +"</ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><REQUEST_ID>" + r_id +"</REQUEST_ID><REQUEST_TIME></REQUEST_TIME><PRO_NAME>hailong</PRO_NAME><PROVINCE_CODE>340000</PROVINCE_CODE><REGION_CODE>340551</REGION_CODE><COUNTY_CODE>340104</COUNTY_CODE><CUST_COMPANY>1003</CUST_COMPANY><BUILD_COMPANY>jianshe</BUILD_COMPANY><DESIGN_COMPANY>sheji</DESIGN_COMPANY><WORKING_COMPANY>shigong</WORKING_COMPANY><SUPERVISOR_COMPANY>jianli</SUPERVISOR_COMPANY><WORKADDRESS></WORKADDRESS><WORKSTARTTIME>2017-07-01</WORKSTARTTIME><WORKENDTIME>2017-08-01</WORKENDTIME><REALITY_DELIVERTIME>2017-09-01</REALITY_DELIVERTIME><DYJPTJ>1</DYJPTJ><SITE_LOC_QK>1</SITE_LOC_QK><HANG_SCOPE>1</HANG_SCOPE><YDDCRL>1</YDDCRL><JWS>1</JWS><KTAZ>1</KTAZ><TDGSFZR>username</TDGSFZR><CHECKTIME>2017-08-08</CHECKTIME><CHECK_PEOPLE>yanshourenyuan</CHECK_PEOPLE></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    u = config.url + "/services/DeliveryInfoSynchronization?wsdl"
    cc = suds.client.Client(u).service.DeliveryInfoSynchronization(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    print ">> 返回报文:\n",jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__ == "__main__":
    for i in range(1):
        for i in range(1):
            t = threading.Thread(target=DI5, args=())
            t.start()
        t.join()
    print ">> program run end"
