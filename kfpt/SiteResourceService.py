#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import suds
import threading
import config

def site():

    print u">> 站址信息查询服务"
    head = """<?xml version="1.0" encoding="UTF-8"?><PACKET>\
<HEAD><CUST_COMPANY>1003</CUST_COMPANY>\
<SERVICE_CODE>T02_OT_001</SERVICE_CODE>\
<ACCESS_TOKEN></ACCESS_TOKEN>\
<REQUEST_TIME>2017-07-11 09:00:00</REQUEST_TIME></HEAD>"""
    body = "<BODY>\
<SITE_CODE></SITE_CODE>\
<PROVINCE_CODE> <PROVINCE_CODE>\
<CITY_CODE></CITY_CODE >\
<CUST_COMPAN ></CUST_COMPANY>\
<START_TIME></START_TIME>\
<END_TIME></END_TIME>\
<REQUEST_TIME></REQUEST_TIME>\
</BODY></PACKET>"

    XML = head + body
    url =  config.url + "/services/SiteResource?wsdl"
    cc = suds.client.Client(url).service.SiteResource(encReqXml='')
    print cc
    #res = cc.service.SiteResource(encReqXml='')
    #print res

''' person = cc.factory.create('ns0:Exception')
    person1 = cc.factory.create('ns0:SiteResource')
    person2 = cc.factory.create('ns0:SiteResourceResponse')
    print person
    print person1
    print person2'''

if __name__ == '__main__':
    tt = []  
    for i in range(1):
        t = threading.Thread(target=site, args=())
        tt.append(t)
        t.setDaemon(True)
        t.start()
