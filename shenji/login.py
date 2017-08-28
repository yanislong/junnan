#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import re

def login(name="chenliang13",passwd="000000"):
    url = "http://123.126.34.238:6080/audituat/main/login/cn.chinatowercom.audit.main.login.login.flow"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36", "Referer":"http://123.126.34.238:6080/audituat/main/login/login.jsp"}
    data = {"original_url":"null","userId":name,"password":passwd}
    r = requests.post(url, headers=header, data=data, allow_redirects=False)
    l1 = re.compile(r"JSESSIONID=(.*?);")
    l2 = l1.findall(str(r.headers))
    print l2[0]
    return l2[0]

if __name__ == "__main__":
    pass
    login()
#    header = {"Cookie":"JSESSIONID=D9E0A5B330027A2FE9CB44D297161180"}
#    r = requests.get("http://123.126.34.238:6080/audituat/main/skins/topbottom/index.jsp", headers=header)
#    print r.content
