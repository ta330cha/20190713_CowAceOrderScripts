##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import threading
import time
from datetime import datetime

import logging as log

def task(self):
    log.LogPrint("Starting buy thread")
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
    #買い注文表から買い注文候補をリストアップする
    #買い注文候補から取引に重複があれば除外
    #買い注文候補から予約注文に重複があれば除外
    #予約注文

#---END---#