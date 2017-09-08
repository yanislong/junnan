#!/usr/bin/python
#-*- coding=utf-8 -*-

import requests
import login
import json

url = "http://123.126.34.238:6080/audituat/plant/annualPlant/cn.com.strongdata.wdf.eos.core.WDFEOSComponent.requestReceive.biz.ext"
header = {}
header['X-Requested-With'] = "XMLHttpRequest"
header['Content-type'] = "application/json"
header["Cookie"] = "JSESSIONID=" + login.login()
#data = {"actionKey":"/paudit/plant/AnnualPlant/judgeAnnualPlantIsExist","dataModelIn":{}}
#data = {"actionKey":"/paudit/plant/AnnualPlant/getMessage","dataModelIn":{}}
data = {"actionKey":"/paudit/plant/AnnualPlant/","dataModelIn":{}}
r = requests.post(url, headers=header, data=json.dumps(data))
print r.content
