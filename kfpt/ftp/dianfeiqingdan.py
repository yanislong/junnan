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
    num = "1000235"
    num2 = ""
    token5 = "MTAwNTExMVQwNl9PVF8wMDU4ODgyMDE3LTA4"
    token3 = "MTAwM2FiY1QwNl9PVF8wMDV4eXoyMDE3LTA4"
    XML1 = "<PACKET><HEAD><SYS_COMPANY>1005</SYS_COMPANY><SERVICE_CODE>T06_OT_005</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>"+token5+"</ACCESS_TOKEN><HANDLE_TYPE>1</HANDLE_TYPE><CUST_COMPANY>1002</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID></FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    XML2 = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T06_OT_005</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>" + token3 + "</ACCESS_TOKEN><HANDLE_TYPE>2</HANDLE_TYPE><CUST_COMPANY>1003</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID>"+ num +"</FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    XML3 = "<PACKET><HEAD><SYS_COMPANY>1005</SYS_COMPANY><SERVICE_CODE>T06_OT_005</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>" + token5 + "</ACCESS_TOKEN><HANDLE_TYPE>3</HANDLE_TYPE><CUST_COMPANY>1002</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID>"+ num +"</FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    XML4 = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T06_OT_005</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>" + token3 + "</ACCESS_TOKEN><HANDLE_TYPE>4</HANDLE_TYPE><CUST_COMPANY>1003</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID>"+ num2 +"</FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    XML = XML3
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    endata = r0.content.replace(r"\n","")
    print "请求报文密文:\n", endata
    print u">> T06-T-O-005 电费清单查询服务"
    print "*************"
    en = endata[1:-1]
    u = config.url + "/services/filesMutual?wsdl"
    cc = suds.client.Client(u).service.ftpFilesMutual(encReqXml=en)
#    res = cc.service.DemandImport(encReqXml=en)
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
