#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import threading
import time
import suds
import sys
sys.path.append('/root/git_20170730/kfpt')
import config
import jiemi
import jiami

def tower():
    print u">> 铁塔信息查询服务"
    XML = "H4sIAAAAAAAAAH1Sy27DIBD8lf5AxNpJmodWSAQ2ipsADl5b9YlTDz31aPXvi+XEDW1VTszMLrsz\nAmulz8QST6SMRN02HLW3tXK9LACWKDIKGwpdpSkRhiRDET1HgBJFJqDSmpomsj+Tk5bVYMvje19c\nB9vt6u64Hax5Wb29fnxaQ8sLqxWKrAUDXVtKg7myJEsoNgvYLJYFikzAg2J9is5LGE9aYyaQPatL\ndK2VqesbJIshkOO78ghRTCkcvBmtVnyzs072ZoB18F3l7lafUeQE6or76VqU41ZpxszkAW9/pcsq\n/PAM6yfY7QH240MPOpIz/1TO6t9JZrV5pGJyL24f4wsZP8uwIQIAAA=="
    url = config.url + "/services/TowerResource?wsdl"
    cc = suds.client.Client(url)
    res = cc.service.TowerResource(encReqXml=XML)
    print res
    print jiemi.jiemi(res.replace(r"\n",""))

    return None

'''
    person = cc.factory.create('ns0:Exception')
    person1 = cc.factory.create('ns0:TowerResource')
    person2 = cc.factory.create('ns0:TowerResourceResponse')
    print person
    print person1
    print person2
'''
if __name__ == "__main__":
    stime = time.ctime()

    for i in range(1):
        ll = []
        for j in range(1):
            t = threading.Thread(target=tower,args=())
            ll.append(t)
        for k in ll:
            k.start()
        for l in ll:
            l.join()
    print stime
    print time.ctime()
    print "end"
