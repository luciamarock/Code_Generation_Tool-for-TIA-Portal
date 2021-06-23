# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:00:55 2021

@author: luciamarock
"""
# g++ -o libinfo.so -shared -fPIC info.cpp
import ctypes

#libInfo = CDLL("./libinfo.so")
libInfo = ctypes.CDLL("./libinfo.so")
 
libInfo.pinfo()
 