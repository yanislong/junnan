#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import suds
import sys
sys.path.append("/root/git_20170730/kfpt")
import jiemi
import config

'''
    head = """<?xml version="1.0" encoding="UTF-8"?><PACKET>\
<HEAD><CUST_COMPANY>1003</CUST_COMPANY>\
<SERVICE_CODE>T02_OT_001</SERVICE_CODE>\
<ACCESS_TOKEN></ACCESS_TOKEN>\
<REQUEST_TIME>2017-07-11 09:00:00</REQUEST_TIME></HEAD>"""

    body = "<SITE_CODE></SITE_CODE>\
<ROOM_ID></ROOM_ID>\
<PROVINCE_CODE> <PROVINCE_CODE>\
<CITY_CODE></CITY_CODE >\
<CUST_COMPAN ></CUST_COMPANY>\
<START_TIME></START_TIME>\
<END_TIME></END_TIME>\
<REQUEST_TIME></REQUEST_TIME>\
</BODY></PACKET>"
'''

def Room():
    print u">> 机房信息查询服务"
    XML = "H4sIAAAAAAAAAJWSQW7DIBBFr+ILVGDHaZ1qhERgolgJ4OCxVa9YdZFVllZvX+ykdlGlSEWz4P+Z\nWbwP0Eh1QhJwRKkFqK6loJxppB1EzvkGWGJBi76vFUZDoyCeB0dhHksa4PHSYdyj2qAoeP72wmNt\nM7575zwWsGQCpFLYtoHcCa0wJEdTHK5DfhlNv2v6QzUabcvPj9uX0bg5kyyBJSuwl6SOwTrBp1MA\nWwwgR/IcbGdE3FpFZPUeLc2CT5yrBDbHkWWwd3qirulBto2ki4j9xru+tj/cr8BSA1RNw/1aFkU1\nga9Omnb1J2qS/lmCv/qAVj+ZXLr/fhd252ePX/INT1Ya9S4CAAA="
    u = config.url + "/services/RoomResource?wsdl"
    cc = suds.client.Client(u)
    res = cc.service.RoomResource(encReqXml=XML)
    print res
    print jiemi.jiemi(res.replace(r"\n",""))
    return None

'''
    person=cc.factory.create('ns0:Exception')
    person1=cc.factory.create('ns0:RoomResource')
    person2=cc.factory.create('ns0:RoomResourceResponse')
    print person
    print person1
    print person2
'''

Room()
