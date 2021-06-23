# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:00:55 2021

@author: luciamarock
"""

from ctypes import *

#libInfo = CDLL("./libinfo.so")
libInfo = cdll.LoadLibrary("libinfo.so")
 
libInfo.pinfo()
 