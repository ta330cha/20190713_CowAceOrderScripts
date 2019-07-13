##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import time
import sys
import os
import threading
from datetime import datetime

#from logging import logging as log

#Threads
from ThreadTimer import ThreadTimer

#Libraries
import Settings

#Load files
SETTING_FILE = "src/settings.ini"

def main():
    print('Working at:{}'.format(os.getcwd()))
    settings = Settings.Settings(SETTING_FILE)
    settings.load_settings()
    interval = settings.Interval
    
    threadTimer = ThreadTimer(interval)
    threadTimer.Start()
    
    while(True):
        print('Watching Thread:{}'.format(str(threading.activeCount())))
        time.sleep(10)

if __name__ == '__main__':
    main()

#---END---