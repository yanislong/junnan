#!/usr/bin/python
# -*- coding=utf-8 -*-

from ftplib import FTP
import threading
import requests
import chardet
import suds
import time
import re
import sys
sys.path.append('/root/git_20170730/kfpt')
import jiami
import config
import jiemi
reload(sys)
sys.setdefaultencoding('utf-8')

flow_id = ""
flow_id2 = ""
def DI1():
    print "######################1上传登记############################"
    global flow_id
    token4 = "MTAwNDAwMFQwNV9PVF8wMDE5OTkyMDE3LTA4"
    XML = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T05_OT_001</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>" + token4 + "</ACCESS_TOKEN><HANDLE_TYPE>1</HANDLE_TYPE><CUST_COMPANY>1003</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID></FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    print u">> 详单查询接口"
    print "*************"
    u = config.url + "/services/filesMutual?wsdl"
    cc = suds.client.Client(u).service.ftpFilesMutual(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    rep = jiemi.jiemi(cc.replace(r"\n",""))
    if "000000" in rep:
        l1 = re.compile(r'<FTP_USER>(.*?)<')
        ll1 = re.compile(r'<FTP_PWD>(\w{2,3}\d{1,6})')
        lll1 = re.compile(r'<FLOW_ID>(\d*)<')
        l2 = l1.findall(rep)
        l3 = ll1.findall(rep)
        l4 = lll1.findall(rep)
        print l2[0],"\t",l3[0],"\t",l4[0]
    else:
        print "error quit"
        sys.exit()
    ftp = FTP()
    ftp.connect('123.126.34.27',"12221")
    try:
        print ">>FTP用户登录..."
        ftp.login(l2[0],l3[0])
        print ftp.getwelcome()
        bufsize = 2048
        up_file = open('/root/long.xlsx','rb')
        try:
            print ">>FTP文件上传..."
            ftp.storbinary('STOR long.xlsx',up_file,bufsize)
        except:
            print "up file error"
            print ">>>>FLOW_ID:\t%s"%l4
            sys.exit()
    except:
        print "login error"
        print ">>>>FLOW_ID:\r%s"% l4
        sys.exit()
    print "######################1上传登记 end############################"
    flow_id = l4[0]
    return None

def DI3():
    print "######################2FTP文件上传完成，销毁上传用户###########################"
    global flow_id
    num = flow_id
    token4 = "MTAwNDAwMFQwNV9PVF8wMDE5OTkyMDE3LTA4"
    XML = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T05_OT_001</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>"+ token4 +"</ACCESS_TOKEN><HANDLE_TYPE>3</HANDLE_TYPE><CUST_COMPANY>1003</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID>"+ num +"</FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    print u">> 详单查询接口"
    print "*************"
    u = config.url + "/services/filesMutual?wsdl"
    cc = suds.client.Client(u).service.ftpFilesMutual(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    rep = jiemi.jiemi(cc.replace(r"\n",""))
    if "000000" not in rep:
        print "error"
    print "######################3FTP文件上传完成，销毁上传用户end############################"
    return None

def DI2():
    print "######################2下载登记 end############################"
    global flow_id2
    token3 = "MTAwM2FiY1QwNV9PVF8wMDF4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T05_OT_001</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>" + token3 + "</ACCESS_TOKEN><HANDLE_TYPE>2</HANDLE_TYPE><CUST_COMPANY>1003</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID></FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    print u">> 详单查询接口"
    print "*************"
    u = config.url + "/services/filesMutual?wsdl"
    cc = suds.client.Client(u).service.ftpFilesMutual(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    rep = jiemi.jiemi(cc.replace(r"\n",""))
    if "000000" in rep:
        l1 = re.compile(r'<FTP_USER>(.*?)<')
        ll1 = re.compile(r'<FTP_PWD>(\w{2,3}\d{1,6})')
        lll1 = re.compile(r'<FLOW_ID>(\d*)<')
        l2 = l1.findall(rep)
        l3 = ll1.findall(rep)
        l4 = lll1.findall(rep)
        print l2[0],"\t",l3[0],"\t",l4[0]
    else:
        print "error quit"
        sys.exit()
    ftp = FTP()
    ftp.connect('123.126.34.27',"12221")
    try:
        print ">>FTP用户登录..."
        ftp.login(l2[0],l3[0])
        print ftp.getwelcome()
        bufsize = 2048
        down_file = open('/root/git_20170730/kfpt/ftp/down/xdcx/'+ str(time.strftime("%Y-%m-%d %X",time.localtime())) +'.xlsx','wb').write
        try:
            print ">>FTP文件下载..."
            ftp.retrbinary('RETR long.xlsx',down_file,bufsize)
        except:
            print "down file error"
            print ">>>>FLOW_ID:\t%s" %l4[0]
            sys.exit()
    except:
        print "login error"
        print ">>>>FLOW_ID:\r%s"% l4
        sys.exit()
    flow_id2 = l4[0]
    print "######################2下传登记 end############################"
    return None

def DI4():
    print "######################4下载完成，销毁下载用户############################"
    global flow_id2
    num2 = flow_id2
    token3 = "MTAwM2FiY1QwNV9PVF8wMDF4eXoyMDE3LTA4"
    XML = "<PACKET><HEAD><SYS_COMPANY>1004</SYS_COMPANY><SERVICE_CODE>T05_OT_001</SERVICE_CODE><FILE_TYPE>JSXD</FILE_TYPE><REQUEST_TIME>2017-07-05 09:00:00</REQUEST_TIME><ACCESS_TOKEN>" + token3 + "</ACCESS_TOKEN><HANDLE_TYPE>4</HANDLE_TYPE><CUST_COMPANY>1003</CUST_COMPANY><ACCOUNT_PERIOD>201704</ACCOUNT_PERIOD><PROVINCE_ID>370000</PROVINCE_ID><CITY_ID>370100</CITY_ID><FLOW_ID>"+ num2 +"</FLOW_ID><STATUS>1</STATUS></HEAD></PACKET>"
    print "请求报文明文:\n", XML
    r0 = requests.post(config.encode, data={'requestXml':XML})
    en = r0.content.replace(r"\n","")[1:-1]
#    print "请求报文密文:\n", en
    print u">> 详单查询接口"
    print "*************"
    u = config.url + "/services/filesMutual?wsdl"
    cc = suds.client.Client(u).service.ftpFilesMutual(encReqXml=en)
#    print "请求返回的加密报文:\n", cc
    rep = jiemi.jiemi(cc.replace(r"\n",""))
    if "000000" not in rep:
        print "error"
    print "######################4下载完成，销毁下载用户end############################"
    return None

if __name__ == "__main__":
#    print time.strftime("%Y-%m-%d",time.localtime())
    DI1()
    DI3()
    DI2()
    DI4()
    for i in range(0):
        for i in range(1):
            t = threading.Thread(target=DI, args=(XML1,))
            t.start()
        t.join()
    print ">> program run end"
