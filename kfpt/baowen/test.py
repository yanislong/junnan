#!/usr/bin/python
# -*- coding=utf-8 -*-

def param():
#    with open('towerR.txt','r') as ff:
#   with open("Demandimport5.txt","r") as ff: # DemandImport
#   with open("dodi.txt","r") as ff: # DemandImport
#   with open("DemandOrderSync.txt","r") as ff: # DemandOrderSync
   with open("demandrec.txt","r") as ff: # DemandOrderSync
#   with open("DemandOrderConfirmationImport.txt","r") as ff: # DemandOrderconfirmationImportServer
        str = ""
        while 1:
            ll = ff.readline()
            if not ll:
                break
            str = str + "<" + ll[:-1] + "></" + ll[:-1] + ">"
        str = "<PACKET><HEAD><CUST_COMPANY>1003</CUST_COMPANY><SERVICE_CODE>T02_OT_001</SERVICE_CODE><ACCESS_TOKEN></ACCESS_TOKEN><REQUEST_TIME>2017-07-31</REQUEST_TIME></HEAD><BODY>" + str + "</BODY></PACKET>"
        print str
        return str

if __name__ == "__main__":
    param()
