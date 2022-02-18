# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:55:19 2022

@author: marszale
"""
from datetime import date, datetime, timedelta
from httpRequestHandler import httpRequestHandler
from apiRequestBuilder import apiRequestBuilder
from getDataFromCSV import getDataFromCSVhandler
from utilityFunctions import intToStrWithZero


import unittest
testuj = 1




class mainCalculator(object):
    
    def __init__(self):
        self.dictIncomeInPlnPerDay = {}
        
    def findKeyFromRateTable(self, rateDict, key):
        
        found = 0
        dayInStringUnderSearch = key
        maxCounter = len(rateDict) + 5
        counter = 0
        
        while(found == 0):
            counter = counter + 1
            if(counter > maxCounter):
                return "error no date"
            splitted = dayInStringUnderSearch.split("-")
            currentDate = date(int(splitted[0]), int(splitted[1]), int(splitted[2]))
            previousDate = currentDate - timedelta(days=1)
            dayInStringUnderSearch = intToStrWithZero(previousDate.year) + "-" + intToStrWithZero(previousDate.month) + "-" + intToStrWithZero(previousDate.day)
            if(dayInStringUnderSearch in rateDict):
                return dayInStringUnderSearch
      
        
    def calculateIncomeInPln(self, rateDict, currencyIncomeDict):
        
        for key, value in currencyIncomeDict.items():
            rateKey = self.findKeyFromRateTable(rateDict, key)
            self.dictIncomeInPlnPerDay[key] = rateDict[rateKey] * currencyIncomeDict[key]
            
            
    def provideSum(self):
        sum = 0
        
        for element in self.dictIncomeInPlnPerDay.values():
            sum = sum + element
            
        return sum
            
        

        








class TestingClass(unittest.TestCase):
  

    
    def test_dataRateSchift1(self):
        calculator = mainCalculator()
        rateDict  = {"2021-10-01": 2, "2021-10-02": 3}
        self.assertEqual(calculator.findKeyFromRateTable(rateDict,"2021-10-03"), "2021-10-02")
        
    def test_dataRateSchift2(self):
        calculator = mainCalculator()
        rateDict  = {"2020-12-31": 2, "2021-10-01": 2, "2021-10-02": 3}
        self.assertEqual(calculator.findKeyFromRateTable(rateDict,"2021-01-01"), "2020-12-31")
        
    def test_incomeInPln1(self):
        calculator = mainCalculator()
        rateDict  = {"2021-09-30": 1, "2021-10-01": 2, "2021-10-02": 3}
        incomeDict = {"2021-10-01": 4, "2021-10-02": 7}
        calculator.calculateIncomeInPln(rateDict, incomeDict)
        self.assertEqual(calculator.dictIncomeInPlnPerDay["2021-10-01"], 4)
 
    def test_incomeInPln2(self):
        calculator = mainCalculator()
        rateDict  = {"2021-10-01": 2, "2021-10-02": 3}
        incomeDict = {"2021-10-02": 4, "2021-10-03": 7}
        calculator.calculateIncomeInPln(rateDict, incomeDict)
        self.assertEqual(calculator.dictIncomeInPlnPerDay["2021-10-03"], 21)
        
    def test_e2e1(self):
        handler = apiRequestBuilder()
        requestText = handler.buildRequest("eur", date(2021, 12, 28), date(2022, 1, 31))
        requestHandler = httpRequestHandler()
        rateDictionary = requestHandler.getCurrencyRatesInDics(requestText)
        fileName = 'tableForTestShort.csv'
        csvHandler = getDataFromCSVhandler()
        incomeDictionary = csvHandler.getIncomeDictionaryFromFile(fileName)
        calculator = mainCalculator()
        calculator.calculateIncomeInPln(rateDictionary, incomeDictionary)
        self.assertEqual(round(calculator.provideSum(),4), round(0.7738,4))
        
        


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)