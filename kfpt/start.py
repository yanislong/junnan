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


def DI():
#    DemandImportService.DI1()
#    DemandReceiveService.DI2()
#    DemandOrderSynchronizationService.DI3()
#    DemandOrderConfirmationImportServer.DI4()
#    DemandOrderDeliveryInformationSynchronizationService.DI5()
#    DemandOrderDeliveryResultImportService.DI6()
    RentNotificationInformationSynchronizationService.DI7()
    ConfirmResultsFromImportService.DI8()
    ProjectConstructionScheduleQueryService.DI9()
    ScreeningResultsFeedbackService.DI10()
    ScreeningValidationResultsImportService.DI11()

if __name__ == "__main__":
    for i in range(0):
        for i in range(1):
            print i
            t = threading.Thread(target=DI, args=())
            t.start()
        t.join()
    print ">> program run end"
