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


def site():
    XML4 = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T01_OT_001</SERVICE_CODE><ACCESS_TOKEN>MTAwM2FiY1QwMV9PVF8wMDF4eXoyMDE3LTA4</ACCESS_TOKEN><REQUEST_TIME>2017-07-11 09:00:00</REQUEST_TIME><BATCH_NO>000004</BATCH_NO><TOTAL_NUM>1</TOTAL_NUM><CURRENT_NUM>1</CURRENT_NUM></HEAD><BODY><SITE_CODE>5</SITE_CODE><PROVINCE_CODE>6</PROVINCE_CODE><CITY_CODE>110000</CITY_CODE><CUST_COMPANY>8</CUST_COMPANY><START_TIME>2017-07-05 09:00:00</START_TIME><END_TIME>2017-07-05 09:00:00</END_TIME><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME></BODY></PACKET>"
    XML = XML4
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    endata = r0.content.replace(r"\n","")
    print "请求报文密文:\n", endata
    print u">> 站址信息查询服务"
    print "*************"
    en = endata[1:-1]
    url =  config.url + "/services/SiteResource?wsdl"
    cc = suds.client.Client(url).service.SiteResource(encReqXml=endata)
    print "请求返回的加密报文:\n", cc
    print jiemi.jiemi(cc.replace(r"\n",""))
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
