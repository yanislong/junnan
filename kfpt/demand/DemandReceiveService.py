#!/usr/bin/python
# -*- coding=utf-8 -*-

import threading
import requests
import chardet
import suds
import sys
reload(sys)
sys.path.append('/root/git_20170730/kfpt')
import jiami
import config
import jiemi
sys.setdefaultencoding('utf-8')

def DI2():
    print u">> T02-T-O-001 需求承接结果反馈服务 "
    print "*************"
    r_id = "1016013001095193"
    token = "MTAwM2FiY1QwMl9UT18wMDF4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T02_TO_001</SERVICE_CODE><ACCESS_TOKEN>"+ token +"</ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><EQUEST_ID>"+ r_id +"</EQUEST_ID><PROVINCE_CODE>340000</PROVINCE_CODE><REGION_CODE>340551</REGION_CODE><COUNTY_CODE>340104</COUNTY_CODE><CUST_COMPANY>1003</CUST_COMPANY><RESULT>1</RESULT><REFUSE_DESC></REFUSE_DESC><CUST_NAME>long</CUST_NAME><IMP_TIME></IMP_TIME><REQUEST_TIME></REQUEST_TIME></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    u = config.url + "/services/DemandReceive?wsdl"
    cc = suds.client.Client(u).service.DemandReceive(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    print ">> 返回报文:\n",jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__ == "__main__":
    for i in range(1):
        print i
        t = threading.Thread(target=DI2, args=())
        t.start()
    t.join()
    print ">> program run end"
