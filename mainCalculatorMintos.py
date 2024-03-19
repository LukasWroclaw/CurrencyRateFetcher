# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:55:19 2022

@author: marszale
"""
from datetime import date, datetime, timedelta
from httpRequestHandler import httpRequestHandler
from apiRequestBuilder import apiRequestBuilder
from getDataFromCSVMintos import getDataFromCSVhandlerMintos
from utilityFunctions import intToStrWithZero


import unittest
testuj = 0




class mainCalculator(object):
    
    def __init__(self):
        self.dictIncomeInPlnPerDay = {}
        self.dictTaxInPlnPerDay = {}
        
    def findKeyFromRateTable(self, rateDict, key):
        found = 0
        dayInStringUnderSearch = key
        maxCounter = 10
        counter = 0
        
        while(found == 0):
            counter = counter + 1
            if(counter > maxCounter):
                print("Debug, cannot found:", dayInStringUnderSearch)
                return "error no date"
            splitted = dayInStringUnderSearch.split("-")
            currentDate = date(int(splitted[0]), int(splitted[1]), int(splitted[2]))
            previousDate = currentDate - timedelta(days=1)
            dayInStringUnderSearch = intToStrWithZero(previousDate.year) + "-" + intToStrWithZero(previousDate.month) + "-" + intToStrWithZero(previousDate.day)
            if(dayInStringUnderSearch in rateDict):
                return dayInStringUnderSearch
      
        
    def calculateIncomeInPln(self, rateDict, currencyDict):
        
        for key, value in currencyDict.items():
            rateKey = self.findKeyFromRateTable(rateDict, key)
            self.dictIncomeInPlnPerDay[key] = rateDict[rateKey] * currencyDict[key]
            
            
    def provideIncomeSum(self):
        sum = 0
        
        for element in self.dictIncomeInPlnPerDay.values():
            sum = sum + element
            
        return sum
    
    def calculateTaxInPln(self, rateDict, currencyDict):
        
        for key, value in currencyDict.items():
            rateKey = self.findKeyFromRateTable(rateDict, key)
            self.dictTaxInPlnPerDay[key] = rateDict[rateKey] * currencyDict[key]
        
    def provideTaxSum(self):
        sum = 0
        
        for element in self.dictTaxInPlnPerDay.values():
            sum = sum + element
            
        return sum

            

print("Start")
handler = apiRequestBuilder()
requestText = handler.buildRequest("eur", date(2023, 9, 28), date(2023, 12, 31))
requestHandler = httpRequestHandler()
rateDictionary = requestHandler.getCurrencyRatesInDics(requestText)
fileName = 'q4.csv' 
csvHandler = getDataFromCSVhandlerMintos()
incomeDictionary, taxDictionary = csvHandler.getIncomeAndTaxDictionaryFromFile(fileName)
calculator = mainCalculator()
calculator.calculateIncomeInPln(rateDictionary, incomeDictionary)
print("Suma zyskow:", calculator.provideIncomeSum())
calculator.calculateTaxInPln(rateDictionary, taxDictionary)
print("Suma podatku za granica:", calculator.provideTaxSum())
        








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
        requestText = handler.buildRequest("eur", date(2023, 3, 31), date(2023, 4, 6))
        requestHandler = httpRequestHandler()
        rateDictionary = requestHandler.getCurrencyRatesInDics(requestText)
        fileName = 'tableForTestShort.csv'
        csvHandler = getDataFromCSVhandlerMintos()
        incomeDictionary, taxDictionary = csvHandler.getIncomeAndTaxDictionaryFromFile(fileName)
        calculator = mainCalculator()
        calculator.calculateIncomeInPln(rateDictionary, incomeDictionary)
        self.assertEqual(round(calculator.provideIncomeSum(),4), round(1.7786,4))
        calculator.calculateTaxInPln(rateDictionary, taxDictionary)
        self.assertEqual(round(calculator.provideTaxSum(),4), round(-0.2339,4))
        
        


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)