#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import urllib2
import json

def post_multipart():
    url = "http://123.126.34.238:6080/audituat/plant/annualPlant/cn.com.strongdata.wdf.eos.module.UploadFileComponent.uploadFileAndOtherHandle.biz.ext"
    content_type, body = encode_mulitpart_formdata()
    req = urllib2.Request(url, body)
    req.add_header("Content-Type",content_type)
    req.add_header("Cookie","JSESSIONID=CC46AC83381FD06B55EE37E5AA612DD7")
    try:
        reponse = urllib2.urlopen(req)
        the_page = reponse.read().decode('utf-8')
        print the_page
        return the_page
    except urllib2.HTTPError,e:
        print e.code
        pass
    except urllib2.URLError, e:
        print str(e)
        pass

def encode_mulitpart_formdata():
    boundary = "--hailong"
    crlf = "\r\n"
    data1 = json.dumps("/paudit/plant/AnnualPlant/add")
    data2 = json.dumps({"annualPlant":{"id":"","relationId":"","menFileId":"","planCode":"SJJH2017","planYear":"2017","planAddpersion":"陈亮","planName":"123","planMain":""}})
    data3 = json.dumps({"wdf-allMaxSize":"104857600","wdf-singleMaxSize":"20971520","wdf-allMaxStr":'',"wdf-singleMaxStr":"","wdf-fileTypes":"","wdf-relationIds":""})
    l = []
    l.append("--" + boundary)
    l.append("Content-Disposition:form-data; name=actionKey")
    l.append('')
    l.append(data1)
    l.append('--' + boundary)
    l.append('')
    l.append("--" + boundary)
    l.append("Content-Disposition:form-data; name=dataModelIn")
    l.append('')
    l.append(data2)
    l.append('--' + boundary)
    l.append('')
    l.append("--" + boundary)
    l.append("Content-Disposition:form-data; name=filesParam")
    l.append('')
    l.append(data3)
    l.append('--' + boundary + "--")
    l.append('')
    body = crlf.join(l)
    content_type = "multipary/form-data; boundary=%s" % boundary
    return content_type, body

if __name__ == "__main__":
    post_multipart()
