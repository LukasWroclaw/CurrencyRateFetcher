# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:48:40 2022

@author: marszale
"""

import csv
import unittest

testuj = 0


class getDataFromCSVHandlerXtb(object):

    def getDataFromFile(self, fileName):
        with open(fileName, mode='r') as csv_file:
            incr = 0;
            listOfRows = []
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                listOfRows.append(row)
                incr+=1
                
            return listOfRows
        
        
handler = getDataFromCSVHandlerXtb()

result = handler.getDataFromFile("xtbTestFileShort.csv")
print(result)