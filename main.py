# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:55:19 2022

@author: marszale
"""
from datetime import date
from httpRequestHandler import httpRequestHandler
from apiRequestBuilder import apiRequestBuilder
from getDataFromCSV import getDataFromCSVhandler
from datetime import date

import unittest
testuj = 1




class mainCalculator(object):
    
    def __init__(self):
        self.dictIncomeInPlnPerDay = {}
        
    def findKeyFromPreviousDay(self, rateDict, key):
        if key in rateDict:
            return key
        
        
        
    
    def calculateIncomeInPln(self, rateDict, currencyIncomeDict):
        
        for key, value in currencyIncomeDict.items():
            self.dictIncomeInPlnPerDay[key] = rateDict[key] * currencyIncomeDict[key]
        

        



"""
handler = apiRequestBuilder()
requestText = handler.buildRequest("eur", date(2021, 12, 28), date(2022, 1, 31))
print(requestText)

requestHandler = httpRequestHandler()
dictionary = requestHandler.getCurrencyRatesInDics(requestText)
print("\nReceived values\n\n")
print(dictionary)

fileName = 'tableForTestShort.csv'
csvHandler = getDataFromCSVhandler()
incomeDictionary = csvHandler.getIncomeDictionaryFromFile(fileName)
print(incomeDictionary)
"""

## suma pln z listy short: 0.773253414148


class TestingClass(unittest.TestCase):
  
    
    def test_incomeInPln1(self):
        calculator = mainCalculator()
        rateDict  = {"2021-10-01": 2, "2021-10-02": 3}
        incomeDict = {"2021-10-01": 4, "2021-10-02": 7}
        calculator.calculateIncomeInPln(rateDict, incomeDict)
        self.assertEqual(calculator.dictIncomeInPlnPerDay["2021-10-01"], 8)
 
    def test_incomeInPln2(self):
        calculator = mainCalculator()
        rateDict  = {"2021-10-01": 2, "2021-10-02": 3}
        incomeDict = {"2021-10-01": 4, "2021-10-03": 7}
        calculator.calculateIncomeInPln(rateDict, incomeDict)
        self.assertEqual(calculator.dictIncomeInPlnPerDay["2021-10-03"], 21)
    


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)