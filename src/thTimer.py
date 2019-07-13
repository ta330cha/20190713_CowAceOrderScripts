##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import threading
import time
from datetime import datetime

import logging as log

#Threads
import thBuy #買い注文スレッド
import thSell #売り注文スレッド
##import thPrev #緊急対策注文スレッド

#Private Val

class thTimer():
    def __init__(self, interval):
        self.__interval = interval
        log.LogPrint('Interval:{}'.format(self.__interval))
        self.__timerNum = 0
        self.__MaxTimerNum = 3
    
    def Start(self):
        log.LogPrint("Starting thread")
        threadTimer = threading.Timer(self.__interval, self.__task)
        threadTimer.start()
        if(self.__timerNum < self.__MaxTimerNum):
            self.__timerNum += 1
        else:
            self.__timerNum = 0
        log.LogPrint("timerNum={}".format(self.__timerNum))
    
    def __task(self):
        if self.__timerNum == 0:
            ##買い注文スレッド
            threadOrder = threading.Timer(1, thBuy.task)
        elif self.__timerNum == 1:
            ##売り注文スレッド
            threadOrder = threading.Timer(1, thSell.task)
        
        ##注文スレッドスタート
        threadOrder.start()
        ##タイマスレッドスタート
        self.Start()

#---END---#