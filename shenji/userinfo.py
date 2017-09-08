#!/usr/bin/python
#-*- coding=utf-8 -*-

import requests
import login
import json

session = login.login()
url = "http://123.126.34.238:6080/audituat/stand/auditResourcePersonInfo/cn.chinatowercom.paudit.stand.auditResourcePersonInfo.updateEmployee.biz.ext"
url1 = "http://123.126.34.238:6080/audituat/stand/auditResourcePersonInfo/cn.chinatowercom.paudit.stand.auditResourcePersonInfo.queryEmployee.biz.ext"
header = {}
header['X-Requested-With'] = "XMLHttpRequest"
header["Cookie"] = "JSESSIONID=" + session
header["Content-Type"] = "text/json"
data = {"relation_id":"","tPauditEmployee":{"empid":100000003,"empname":"高春雷a","empIsWithin":"否","empCompanyName":"test集团总部(本部)","empSex":"03","empPost":"","empBranch":"10002","empEducation":"03","empMajor":"","empSchool":"","empTel":"yuejuan","empEmail":"'<br />yuejuan'","empPrice":"","empJobnumber":"10001","empAuditTime":"","empRegion":""}}
#data = {"relation_id":"","tPauditEmployee":{"empid":11465,"empname":"陈亮1","empIsWithin":"否","empCompanyName":"集团总部(本部)","empSex":"10","empPost":"","empBranch":"10001","empEducation":"","empMajor":"","empSchool":"abc","empTel":"abc","empEmail":"abc","empPrice":"","empJobnumber":"","empAuditTime":"","empRegion":""}}
data1 = {"empname":"","empCompanyName":"","empBranch":"","pageIndex":0,"pageSize":8,"sortField":"","sortOrder":"","page":{"begin":0,"length":8}}
r = requests.post(url, headers=header, data=json.dumps(data))
print r.content
header["Content-Type"] = "application/json"
r1 = requests.post(url1, headers=header, data=json.dumps(data1))
print r.content
