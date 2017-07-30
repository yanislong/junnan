#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import suds

def tower():

    print u">> 铁塔信息查询服务"
    
    head = """<?xml version="1.0" encoding="UTF-8"?><PACKET>\
<HEAD><CUST_COMPANY>1003</CUST_COMPANY>\
<SERVICE_CODE>T02_OT_001</SERVICE_CODE>\
<ACCESS_TOKEN></ACCESS_TOKEN>\
<REQUEST_TIME>2017-07-11 09:00:00</REQUEST_TIME></HEAD>"""

    body = "<BODY>\
<SITE_CODE></SITE_CODE>\
<TOWER_CODE></TOWER_CODE>\
<PROVINCE_CODE> <PROVINCE_CODE>\
<CITY_CODE></CITY_CODE >\
<CUST_COMPAN ></CUST_COMPANY>\
<START_TIME></START_TIME>\
<END_TIME></END_TIME>\
<REQUEST_TIME></REQUEST_TIME>\
</BODY></PACKET>"

    XML = head + body

    url = "http://123.126.34.27:18911/services/TowerResource?wsdl"
    cc = suds.client.Client(url)
    print cc
    res = cc.service.TowerResource(encReqXml=XML)
    print res

    person = cc.factory.create('ns0:Exception')
    person1 = cc.factory.create('ns0:TowerResource')
    person2 = cc.factory.create('ns0:TowerResourceResponse')
    print person
    print person1
    print person2

tower()
