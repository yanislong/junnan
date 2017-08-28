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

def DI9():
    print u">> T04-O-T-001 项目建设进度查询服务"
    print "*************"
    r_id = "1217081000015533"
    token = "MTAwM2FiY1QwNF9PVF8wMDF4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T04_OT_001</SERVICE_CODE><ACCESS_TOKEN>"+ token +"</ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><PROVINCE_CODE>340000</PROVINCE_CODE><CITY_CODE>340551</CITY_CODE><CONTRY_CODE>340104</CONTRY_CODE><REQUEST_ID>" + r_id + "</REQUEST_ID><CUSTOMER>1003</CUSTOMER><SITE_CODE>1</SITE_CODE><STARTTIME>2017-10-10 10:10:10</STARTTIME><ENDTIME>2017-10-10 10:10:10</ENDTIME><REQUEST_TIME>2017-10-10 10:10:10</REQUEST_TIME></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    u = config.url + "/services/ScheduleQuery?wsdl"
    cc = suds.client.Client(u).service.ScheduleQuery(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    print ">> 返回报文:\n",jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__ == "__main__":
    for i in range(1):
        for i in range(1):
            t = threading.Thread(target=DI9, args=())
            t.start()
        t.join()
    print ">> program run end"
