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
    print u">> 6.3.3.	T02-T-O-002 筛查结果反馈服务"
    print "*************"
    r_id = "1000235"
    token5 = "MTAwNTExMVQwNl9PVF8wMDU4ODgyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T02_TO_002</SERVICE_CODE><ACCESS_TOKEN>MTAwM2FiY1QwMl9UT18wMDJ4eXoyMDE3LTA4</ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><REQUEST_TIME></REQUEST_TIME><PROVINCE>34</PROVINCE><CITY>340551</CITY><COUNTY></COUNTY><REQUEST_ID>"+r_id +"</REQUEST_ID><CUSTOMER>1003</CUSTOMER><SITE_CHECK_RESULT>1</SITE_CHECK_RESULT><SITE_CHECK_FAIL_INFO>no have</SITE_CHECK_FAIL_INFO><IS_SHARE>1</IS_SHARE><SITE_CODE></SITE_CODE><SITE_NAME></SITE_NAME><LONGITUDE></LONGITUDE><DIMENSION></DIMENSION><ADDRESS></ADDRESS><HANG_SCOPE></HANG_SCOPE><ANTENNA_NUM></ANTENNA_NUM><TOWER_TYPE></TOWER_TYPE><ROOM_TYPE></ROOM_TYPE><BUILD_TYPE></BUILD_TYPE><CREATOR></CREATOR><CHECKTIME></CHECKTIME><REMARK></REMARK></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
    print "请求报文密文:\n", en
    u = config.url + "/services/ScreeningResultsFeedback?wsdl"
    cc = suds.client.Client(u).service.ScreeningResultsFeedback(encReqXml=en)
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
