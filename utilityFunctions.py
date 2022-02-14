# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:36:45 2022

@author: marszale
"""

def intToStrWithZero(inputNumber):
    number = int(inputNumber)
        
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)