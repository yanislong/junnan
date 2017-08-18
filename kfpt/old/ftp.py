#!/usr/bin/python
# -*- coding:utf-8 -*-

from ftplib import FTP
import os

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect("123.126.34.27","12221")
for i in range(1):
    try:
        ftp.login("TTuser7017","791241")
        print "ok"
    except:
        print "no"    
print ftp.getwelcome()
print "****************come in path"
ftp.cmd("/tmp/")
ftp.retrlines('LIST')
ftp.cwd("")
print "************ show file"
ftp.dir('/tmp/')
print "**********show now dir"
ftp.pwd()
print "*************show filler file"
ftp.nlst
bufsize = 1024
filename ="long1.xlsx"
file_handle = open("/root/long.xlsx","rb")
down_file = open("./down","wb").write
#ftp.storbinary('STOR %s' % os.path.basename(filename),file_handle,bufsize)
ftp.storbinary('STOR /home/main_admin/long.txt',file_handle,bufsize)
ftp.retrbinary("RETR %s" % os.path.basename(filename),down_file,bufsize)
ftp.set_debuglevel(0)
file_handle.close()
ftp.quit

print ">>>>>..end..<<<<<<"
