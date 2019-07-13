##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import time
import sys
import os
import threading
from datetime import datetime

import logging as log

#Threads
from thTimer import thTimer

#Libraries
import Settings

#Interval Setting
INTERVAL_SETTING_FILE = "src/Settings/settings.ini"

def main():
    log.LogPrint('Working at:{}'.format(os.getcwd()))
    settings = Settings.Settings(INTERVAL_SETTING_FILE)
    settings.load_settings()
    interval = settings.Interval
    
    threadTimer = thTimer(interval)
    threadTimer.Start()
    
    while(True):
        log.LogPrint('Watching Thread:{}'.format(str(threading.activeCount())))
        time.sleep(60)

if __name__ == '__main__':
    main()

#---END---#