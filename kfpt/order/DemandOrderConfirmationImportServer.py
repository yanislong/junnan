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

def DI():
    print u">> T03-O-T-001 需求订单确认结果导入服务"
    print "*************"
    num = "1000198"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T03_OT_001</SERVICE_CODE><ACCESS_TOKEN></ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><REQUEST_ID></REQUEST_ID><PROVINCE_CODE></PROVINCE_CODE><REGION_CODE></REGION_CODE><COUNTY_CODE></COUNTY_CODE><CUST_COMPANY></CUST_COMPANY><SYNC_RESULT></SYNC_RESULT><FAIL_MESSAGE></FAIL_MESSAGE><CREATOR></CREATOR><CREATETIME></CREATETIME><REQUEST_TIME></REQUEST_TIME></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
    print "请求报文密文:\n", en
    u = config.url + "/services/DemandOrderConfirmationImport?wsdl"
    cc = suds.client.Client(u)#.service.ftpFilesMutual(encReqXml=en)
    print "请求返回的加密报文:\n", cc
    print jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__ == "__main__":
    for i in range(1):
        for i in range(1):
            t = threading.Thread(target=DI, args=())
            t.start()
        t.join()
    print ">> program run end"
