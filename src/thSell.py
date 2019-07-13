##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import threading
import time
from datetime import datetime

import logging as log

def task(self):
    log.LogPrint("Starting sell thread")
    ##---予測データ取得---##
    #maxVal = 109.000 # 高値
    #minVal = 106.000 # 底値   
    ##---市場情報取得---##
    #buyVal =  108.600 # 買値
    #sellVal = 108.300 # 売値
    ##---取引状況---##
    #tradeData = ポジション状況
    ##---予約注文状況---##
    #orderData = 予約注文状況
    #売値の注文が取引に重複があればスキップ
    #売値の注文が予約注文に重複があればスキップ
    #現在の売値で成行注文、T/P=底値とする

#---END---#