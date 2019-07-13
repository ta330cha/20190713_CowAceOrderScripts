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

class Settings:
    def __init__(self, filename):
        self.__INTERVAL = "Interval"
        self.__INTERVAL_ORDER = "IntervalOrder"
        self.__INTERVAL_GETDATA = "IntervalGetData"
        self.__MAXSETTINGCHAR = 256
        self.__filename = filename
        self.Interval = 1000
    
    def __get_pos_setting(self, lines, setting_name):
        ss = 0
        tempList = []
        tempList.append(setting_name)
        for line in lines:
            tt = 0
            temp = setting_name in tempList
            log.LogPrint('line={}'.format(line))
            log.LogPrint('setting_name in line={}'.format(temp))
            if temp:
                while(line[tt] != '='):
                    tt+=1
                return ss, (tt+2)
            else:
                ss+=1
        return -1, -1
    
    def __get_setting_var(self, lines, setting_name):
        temp_list = []
        setting_line, setting_pos = self.__get_pos_setting(lines, setting_name)
        log.LogPrint('setting_line={}'.format(setting_line))
        log.LogPrint('setting_pos={}'.format(setting_pos))
        if setting_line != 0 and setting_pos != 0:
            return 0
        line = lines[setting_line]

        for tt in range(setting_pos, self.__MAXSETTINGCHAR):
            if line[tt] != '\n':
                temp_list.append(line[tt])
            else:
                break
        temp_var = ''.join(temp_list)
        return int(temp_var)
    
    def __get_setting(self, setting_name):
        with open(self.__filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return(self.__get_setting_var(lines, setting_name))

    def __get_interval(self):
        setting_name = self.__INTERVAL
        return self.__get_setting(setting_name)
    
    def load_settings(self):
        log.LogPrint('Setting filename:{}'.format(self.__filename))
        self.Interval = self.__get_interval()
        return 1

def test():
    settings_file = "settings.ini"
    print('Get Settings from Setting filename:{}'.format(settings_file))
    settings = Settings(settings_file)
    print(settings.load_settings())

#---END---#