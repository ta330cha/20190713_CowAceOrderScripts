##!/usr/bin/env python
# -*- coding: utf-8 -*-

logFileName = "src/System.log"

def printLog(text):
    with open(logFileName, 'a', encoding='utf-8') as file:
        file.write(text)

#---END---