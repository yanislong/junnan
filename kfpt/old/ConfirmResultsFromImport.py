#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import suds
import config

'''
    head = """<?xml version="1.0" encoding="UTF-8"?><PACKET>\
<HEAD><CUST_COMPANY>1003</CUST_COMPANY>\
<SERVICE_CODE>T02_OT_001</SERVICE_CODE>\
<ACCESS_TOKEN></ACCESS_TOKEN>\
<REQUEST_TIME>2017-07-11 09:00:00</REQUEST_TIME></HEAD>"""

    body = "<BODY>\
<REQUEST_ID></REQUEST_ID>\
<PROVINCE_CODE></PROVINCE_CODE>\
<REGION_CODE></REGION_CODE>\
<COUNTY_CODE></COUNTY_CODE>\
<CUST_COMPANY></CUST_COMPANY>\
<SYNC_RESULT></SYNC_RESULT>\
<FAIL_MESSAGE></FAIL_MESSAGE>\
<CREATOR></CREATOR>\
<CREATETIME></CREATETIME>\
<REQUEST_TIME></REQUEST_TIME>\
</BODY></PACKET>"
'''

def ConfirmResultsFromImport():

    print u">>起租确认结果导入服务"
    XML = ""
    u = config.url + "/services/RentNotificationInformationSynchronization?wsdl"
    cc = suds.client.Client(u)
#    print cc
    res = cc.service.DeliveryResultImport(encReqXml=XML)
    print res

'''
    person=cc.factory.create('ns0:Exception')
    person1=cc.factory.create('ns0:DeliveryResultImport')
    person2=cc.factory.create('ns0:DeliveryResultImportResponse')
    print person
    print person1
    print person2
'''

ConfirmResultsFromImport()
