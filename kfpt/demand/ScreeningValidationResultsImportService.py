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

def DI11():
    print u">> 筛查确认结果导入服务"
    print "*************"
    r_id = "1217080900015410a"
    token = "MTAwM2FiY1QwMl9PVF8wMDJ4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T02_OT_002</SERVICE_CODE><ACCESS_TOKEN>"+ token + "</ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><REQUEST_ID>"+ r_id +"</REQUEST_ID><PROVINCE_CODE>340000</PROVINCE_CODE><REGION_CODE>340551</REGION_CODE><COUNTY_CODE>340104</COUNTY_CODE><CUST_COMPANY>1003</CUST_COMPANY><SYNC_RESULT>1</SYNC_RESULT><FAIL_MESSAGE></FAIL_MESSAGE><CREATOR>abc</CREATOR><CREATETIME>2017-08-15 19:00:00</CREATETIME><REQUEST_TIME>2017-8-15 12:00:00</REQUEST_TIME></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    u = config.url + "/services/ScreeningValidationResultsImport?wsdl"
    cc = suds.client.Client(u).service.ScreeningValidationResultsImport(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    print ">> 返回报文:\n",jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__ == "__main__":
    for i in range(1):
        for i in range(1):
            t = threading.Thread(target=DI11, args=())
            t.start()
        t.join()
    print ">> program run end"
