#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import time
import suds
import threading
import sys
sys.path.append("/root/git_20170730/kfpt/")
import jiami
import jiemi
import config
import lubin

def site():
    print u">> 机房信息查询服务"
    print "*************"
    token = "MTAwM2FiY1QwMV9PVF8wMDN4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T01_OT_003</SERVICE_CODE><ACCESS_TOKEN>"+ token +"</ACCESS_TOKEN><REQUEST_TIME>2017-07-11 09:00:00</REQUEST_TIME><BATCH_NO>000004</BATCH_NO><TOTAL_NUM>1</TOTAL_NUM><CURRENT_NUM>1</CURRENT_NUM></HEAD><BODY><SITE_CODE></SITE_CODE><ROOM_CODE>005102050200000039498140</ROOM_CODE><PROVINCE_CODE>230000</PROVINCE_CODE><CITY_CODE>231200</CITY_CODE><CUST_COMPANY>1003</CUST_COMPANY><START_TIME>2017-07-05 09:00:00</START_TIME><END_TIME>2017-07-05 09:00:00</END_TIME><REQUEST_TIME>2017-08-09 00:00:00</REQUEST_TIME></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
#    url =  config.url + "/services/RoomResource?wsdl"
    url =  lubin.url + "/services/RoomResource?wsdl"
    cc = suds.client.Client(url).service.RoomResource(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    print ">> 返回报文:\n",jiemi.jiemi(cc.replace(r"\n",""))
    return cc

if __name__ == '__main__':

    stime = time.ctime()
    for i in range(1):
        ll = []
        for i in range(1):
            t = threading.Thread(target=site, args=())
#            tt.append(t)
#            t.setDaemon(True)
            ll.append(t)
        for j in ll:
            j.start()
        for k in ll:
            k.join()
    print stime
    print time.ctime()
    print ">>end"
