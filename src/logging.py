##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import time
import sys
import os
import threading
from datetime import datetime

logFileName = "src/Logs/System.log"

def LogPrint(text):
    with open(logFileName, 'a', encoding='utf-8') as file:
        nowTime = datetime.now().strftime("%Y/%m/%d %H:%M.%S")
        temp = nowTime + " : " + text + "\n"
        file.write(temp)

#---END---#