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
    print u">> T03-O-T-003 起租确认结果导入服务"
    print "*************"
    num = "1000198"
    XML1 = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T05_OT_001</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>MTAwNDAwMFQwNV9PVF8wMDE5OTkyMDE3LTA4</ACCESS_TOKEN><HANDLE_TYPE>1</HANDLE_TYPE><CUST_COMPANY>1002</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID>"+ num +"</FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
    print "请求报文密文:\n", en
    u = config.url + "/services/ConfirmResultsFromImport?wsdl"
    cc = suds.client.Client(u).service.ftpFilesMutual(encReqXml=en)
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
