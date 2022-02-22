# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:48:40 2022

@author: marszale



### dict key = day + symbol, elements: date, symbol, dividend, dividendTax
"""

import csv
from utilityFunctions import intToStrWithZero
import unittest

testuj = 1

class getDataFromCSVHandlerXtb(object):

    def getDataFromFile(self, fileName):
        with open(fileName, mode='r') as csv_file:
            incr = 0;
            listOfRows = []
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                listOfRows.append(row)
                incr+=1
                
            return listOfRows
        
    def convertTime(self, inputTime):
        splitted = inputTime.split(".")
        day = int(splitted[0])
        month = int(splitted[1])
        year = int((splitted[2])[:4])
        return  str(year) + "-" + intToStrWithZero(month) + "-" + intToStrWithZero(day)
    
    def addOrUpdateRecord(self, dictionary, date, symbol, amount):
        key = date + " " + symbol
        
        if amount > 0:
            newDiv = amount
            newTax = 0
        else:
            newDiv = 0
            newTax = abs(amount)
        
        if key not in dictionary:
            dictionary[key] = {"date": date, "symbol": symbol, "dividend": newDiv, "tax": newTax}
        else:
            (dictionary[key])["dividend"] = (dictionary[key])["dividend"] + newDiv
            (dictionary[key])["tax"] = (dictionary[key])["tax"] + newTax
            
            

        
    def buildDictOfRecords(self, rawDataDict):
        
        result = {}
        
        for element in rawDataDict:
            date = self.convertTime(element["Time"])
            symbol = element["Symbol"]
            amount = float(element["Amount"])
            
            self.addOrUpdateRecord(result, date, symbol, amount)
 
        
        
        ##result["2021-11-01 ZW.US"] = {"date": "2021-11-01", "symbol": "ZW.US", "dividend": 10.18, "tax": 3.06}
        return result




class TestingClass(unittest.TestCase):
    
    def test_basicFileRead(self):
            fileName = "xtbTestFileShort.csv"
            handler = getDataFromCSVHandlerXtb()
            rawDictionary = handler.getDataFromFile(fileName)
            self.assertEqual(len(rawDictionary), 8)
            
    def test_convertTime1(self):
            inputTime = "20.10.2021 12:00:00"
            expectedOutput = "2021-10-20"
            handler = getDataFromCSVHandlerXtb()
            result = handler.convertTime(inputTime)
            self.assertEqual(expectedOutput, result)
            
    def test_buildRecord1(self):
            fileName = "xtbTestFileShort.csv"
            handler = getDataFromCSVHandlerXtb()
            rawDictionary = handler.getDataFromFile(fileName)
            expectedDictionary = {"date": "2021-11-01", "symbol": "ZW.US", "dividend": 10.18, "tax": 3.06}
            dictOfRecords = handler.buildDictOfRecords(rawDictionary)
            self.assertEqual(expectedDictionary, dictOfRecords["2021-11-01 ZW.US"])
            
    def test_buildRecord2(self):
            fileName = "xtbTestFileShort.csv"
            handler = getDataFromCSVHandlerXtb()
            rawDictionary = handler.getDataFromFile(fileName)
            expectedDictionary = {"date": "2021-10-20", "symbol": "TLE.NO", "dividend": 29.72, "tax": 7.44}
            dictOfRecords = handler.buildDictOfRecords(rawDictionary)
            self.assertEqual(expectedDictionary, dictOfRecords["2021-10-20 TLE.NO"])
    
    
    
    
    
if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)  