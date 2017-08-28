#!/usr/bin/python
# -*- coding=utf-8 -*-

import threading
import requests
import chardet
import suds
import sys
reload(sys)
sys.path.append("/root/git_20170730/kfpt/")
sys.path.append("/root/git_20170730/kfpt/demand")
sys.path.append("/root/git_20170730/kfpt/order")
sys.path.append("/root/git_20170730/kfpt/project")
sys.path.append("/root/git_20170730/kfpt/ftp")
sys.setdefaultencoding('utf-8')
import config
import jiami
import jiemi
import DemandImportService
import DemandReceiveService
import ConfirmResultsFromImportService
import DemandOrderSynchronizationService
import DemandOrderConfirmationImportServer
import xiangdanchaxun
import ProjectConstructionScheduleQueryService
import DemandOrderConfirmationImportServer
import DemandOrderDeliveryInformationSynchronizationService
import DemandOrderDeliveryResultImportService
import RentNotificationInformationSynchronizationService
import ScreeningResultsFeedbackService
import ScreeningValidationResultsImportService
import dianfeiqingdan
import fuwuzhongzhi
import querenfeiyong
import duizhangqueren
import piliangqizu
import xiangdanchaxun
import yewubiangeng

def DI():
    DemandImportService.DI1()
    DemandReceiveService.DI2()
    DemandOrderSynchronizationService.DI3()
    DemandOrderConfirmationImportServer.DI4()
    DemandOrderDeliveryInformationSynchronizationService.DI5()
    DemandOrderDeliveryResultImportService.DI6()
    RentNotificationInformationSynchronizationService.DI7()
    ConfirmResultsFromImportService.DI8()
    ProjectConstructionScheduleQueryService.DI9()
    ScreeningResultsFeedbackService.DI10()
    ScreeningValidationResultsImportService.DI11()

def ff():
    dianfeiqingdan.DI1()
    fuwuzhongzhi.DI1()
    querenfeiyong.DI1()
    duizhangqueren.DI1()
    piliangqizu.DI1()
    xiangdanchaxun.DI1()
    yewubiangeng.DI1()
    dianfeiqingdan.DI3()
    fuwuzhongzhi.DI3()
    querenfeiyong.DI3()
    duizhangqueren.DI3()
    piliangqizu.DI3()
    xiangdanchaxun.DI3()
    yewubiangeng.DI3()
    dianfeiqingdan.DI2()
    fuwuzhongzhi.DI2()
    querenfeiyong.DI2()
    duizhangqueren.DI2()
    piliangqizu.DI2()
    xiangdanchaxun.DI2()
    yewubiangeng.DI2()
    dianfeiqingdan.DI4()
    fuwuzhongzhi.DI4()
    querenfeiyong.DI4()
    duizhangqueren.DI4()
    piliangqizu.DI4()
    xiangdanchaxun.DI4()
    yewubiangeng.DI4()

if __name__ == "__main__":
    for i in range(30):
        for i in range(5):
            print i
            t = threading.Thread(target=ff(), args=())
            t.start()
        t.join()
''' 
            t = threading.Thread(target=duizhangqueren.DI1(), args=())
            t = threading.Thread(target=duizhangqueren.DI3(), args=())
            t = threading.Thread(target=duizhangqueren.DI2(), args=())
            t = threading.Thread(target=duizhangqueren.DI4(), args=())
            t = threading.Thread(target=yewubiangeng.DI1(), args=())
            t = threading.Thread(target=yewubiangeng.DI3(), args=())
            t = threading.Thread(target=yewubiangeng.DI2(), args=())
            t = threading.Thread(target=yewubiangeng.DI4(), args=())
'''
#    print ">> program run end"
