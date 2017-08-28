#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import sys
sys.path.append('/root/git_20170730/shenji')
import login
import json

url = "http://123.126.34.238:6080/audituat/actualize/exportAudit/cn.chinatowercom.audit.actualize.exportAuditTable.queryAuditTable.biz.ext"
header = {"X-Requested-With":"XMLHttpRequest", "Cookie":"JSESSIONID="+login.login(), "Referer":"http://123.126.34.238:6080/audituat/actualize/exportAudit/AuditResultExportListNew.jsp", "Content-Type":"application/json;charset=UTF-8"}
data = {"criteria/_entity":"cn.chinatowercom.audit.actualize.actualizeData.tAuditPrjInfo","userId":"100002063","criteria/_expr[12]/tAuditPrjInfo.province":"","criteria/_expr[12]/_op":"like","criteria/_expr[17]/tAuditPrjInfo.city":"","criteria/_expr[17]/_op":"like","criteria/_expr[18]/tAuditPrjInfo.county":"","criteria/_expr[18]/_op":"like","criteria/_expr[13]/tAuditPrjInfo.problemType":"","criteria/_expr[13]/_op":"like","criteria/_expr[14]/tAuditPrjInfo.problemName":"","criteria/_expr[14]/_op":"like","criteria/_expr[3]/tAuditPrjInfo.auditLinkman":"","criteria/_expr[3]/_op":"like","criteria/_expr[1]/tAuditPrjInfo.auditCode":"","criteria/_expr[1]/_op":"like","criteria/_expr[5]/tAuditPrjInfo.prjCode":"","criteria/_expr[5]/_op":"like","criteria/_expr[15]/tAuditPrjInfo.auditReportCode":"","criteria/_expr[15]/_op":"like","criteria/_expr[2]/tAuditPrjInfo.auditName":"","criteria/_expr[2]/_op":"like","criteria/_expr[7]/tAuditPrjInfo.projectName":"","criteria/_expr[7]/_op":"like","criteria/_expr[4]/tAuditPrjInfo.orgId":"","criteria/_expr[4]/_op":"=","proStatus":"","criteria/_expr[6]/tAuditPrjInfo.feeName":"","criteria/_expr[6]/_op":"like","criteria/_expr[19]/tAuditPrjInfo.model":"","criteria/_expr[19]/_op":"like","criteria/_expr[8]/tAuditPrjInfo.assignBeg":"","criteria/_expr[9]/tAuditPrjInfo.assingEnd":"","criteria/_expr[10]/tAuditPrjInfo.assignBeg1":"","criteria/_expr[11]/tAuditPrjInfo.assingEnd1":"","criteria/_expr[16]/tAuditPrjInfo.isCheckCut":"","criteria/_expr[16]/_op":"like","pageIndex":0,"pageSize":1,"sortField":"","sortOrder":"","page":{"begin":0,"length":10}}

r = requests.post(url, headers=header, data=json.dumps(data))
print r.content
