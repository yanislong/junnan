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
    print u">> 需求订单同步服务"
    print "*************"
    num = ""
    token = "MTAwNDAwMFQwNV9PVF8wMDI5OTkyMDE3LTA4"
    XML = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T03_TO_001</SERVICE_CODE><ACCESS_TOKEN></ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY><PROVINCE_CODE></PROVINCE_CODE><REGION_CODE></REGION_CODE><COUNTY_CODE></COUNTY_CODE><REQUEST_ID></REQUEST_ID><CUST_COMPANY></CUST_COMPANY><SITE_CODE></SITE_CODE><SITE_NAME></SITE_NAME><SITE_IS_SHARE></SITE_IS_SHARE><LONGITUDE></LONGITUDE><DIMENSION></DIMENSION><ADDRESS></ADDRESS><HANG_SCOPE></HANG_SCOPE><ANT_NUM></ANT_NUM><TOWER_TYPE></TOWER_TYPE><ROOM_TYPE></ROOM_TYPE><BUILD_TYPE></BUILD_TYPE><IN_TYPE></IN_TYPE><REMARK></REMARK><CUSTOMER_NUMBER></CUSTOMER_NUMBER><NEW_CUSTOMER_NUMBER></NEW_CUSTOMER_NUMBER><TOWER_TYPE_DETAIL></TOWER_TYPE_DETAIL><TOWER_HEIGHT></TOWER_HEIGHT><SYSTEM_NUMBER></SYSTEM_NUMBER><BBU_NUM></BBU_NUM><RRU_NUM></RRU_NUM><ELECTRIC_TYPE></ELECTRIC_TYPE><GUARANTEE_TIME></GUARANTEE_TIME><windFactor></windFactor><IS_YDFD></IS_YDFD><PRO_CONFIG></PRO_CONFIG><WBTXGS></WBTXGS><WBTXGH></WBTXGH><WLANAP_NUM></WLANAP_NUM><WLANAP_HEIGHT></WLANAP_HEIGHT><PRO_SYSTEM_NAME></PRO_SYSTEM_NAME><PRO_TX_HEIGHT></PRO_TX_HEIGHT><PRO_TX_NUM></PRO_TX_NUM><PRO_RRU></PRO_RRU><PRO_BBU></PRO_BBU><PRO_SYSTEM_NAME></PRO_SYSTEM_NAME><PRO_TX_HEIGHT></PRO_TX_HEIGHT><PRO_TX_NUM></PRO_TX_NUM><PRO_RRU></PRO_RRU><PRO_BBU></PRO_BBU><PRO_SYSTEM_NAME></PRO_SYSTEM_NAME><PRO_TX_HEIGHT></PRO_TX_HEIGHT><PRO_TX_NUM></PRO_TX_NUM><PRO_RRU></PRO_RRU><PRO_BBU></PRO_BBU><REQUEST_TIME></REQUEST_TIME></BODY></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
    print "请求报文密文:\n", en
    u = config.url + "/services/DemandOrderSynchronization?wsdl"
    cc = suds.client.Client(u).service.DemandImport(encReqXml=en)
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
