##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import threading
import time
from datetime import datetime

import logging as log

#Threads
##import buyThread #買い注文スレッド
##import sellThread #売り注文スレッド
##import prevThread #売り注文スレッド

#Private Val

class ThreadTimer():
    def __init__(self, interval):
        self.__interval = interval
        print('Interval:{}'.format(self.__interval))

        self.__timerNum = 0
    
    def Start(self):
        print("Starting thread at:{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S")))
        thread = threading.Timer(self.__interval, self.__task)
        thread.start()
        print("timerNum={}".format(self.__timerNum))
        self.__timerNum += 1
    
    def __task(self):
        self.Start()

#---END---