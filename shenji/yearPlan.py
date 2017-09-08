#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import login
import json

def Yplan():
    url = "http://123.126.34.238:6080/audituat/plant/annualPlant/cn.com.strongdata.wdf.eos.module.UploadFileComponent.uploadFileAndOtherHandle.biz.ext"
    header = {}
    header['Cookie'] = "JSESSIONID="+login.login("gaochl","000000")
#    header['Cookie'] = "JSESSIONID=5652A81EEFD11C90E4DB2B84DDC367BF"
#    header["X-Requested-With"] = "XMLHttpRequest"
#    boundary = "33591678"
#    header["Content-Type"] = "multipart/form-data;boundary=" + boundary
#    data = "--" + boundary + "\r\nContent-Disposition: form-data; name='actionKey'\r\n\r\n" + "/paudit/plant/AnnualPlant/add" + "\r\n--" + boundary +'\r\nContent-Disposition: form-data; name="dataModelIn"\r\n\r\n' + '{"annualPlant":{"id":"","relationId":"","menFileId":"","planCode":"SJJH2017","planYear":"2017","planAddpersion":"陈亮","planName":"123","planMain":""}}' + '\r\n--' + boundary +'\r\nContent-Disposition: form-data; name="filesParam"\r\n\r\n' + '{"wdf-allMaxSize":"104857600","wdf-singleMaxSize":"20971520","wdf-allMaxStr":"","wdf-singleMaxStr":"","wdf-fileTypes":"","wdf-relationIds":""}' +'\r\n--' + boundary + "--\r\n"
    data = {"actionKey":("","/paudit/plant/AnnualPlant/add",),"dataModelIn":("",json.dumps({"annualPlant":{"id":"","relationId":"","menFileId":"","planCode":"SJJH2017","planYear":"2017","planAddpersion":"陈亮","planName":"123","planMain":""}})),"filesParam":("",json.dumps({"wdf-allMaxSize":"104857600","wdf-singleMaxSize":"20971520","wdf-allMaxStr":"","wdf-singleMaxStr":"","wdf-fileTypes":"","wdf-relationIds":""}))}
    r = requests.post(url, headers=header, files=data, allow_redirects=True)
    print r.content

if __name__ == "__main__":
    Yplan()
