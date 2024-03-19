# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:55:19 2022

@author: marszale
"""
from datetime import date, datetime, timedelta
from httpRequestHandler import httpRequestHandler
from apiRequestBuilder import apiRequestBuilder
from getDataFromOneColumnCSV import getDataFromOneColumnCSV
from utilityFunctions import intToStrWithZero
from saveResultsToCSV import csvWriterClass


import unittest
testuj = 0




class mainCalculator(object):
    
    def __init__(self):
        self.dictIncomeInPlnPerDay = {}
        
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
      
        
    def mapRateToDate(self, rateDict, datesList):
        
        listWithRates = []
        
        
        for element in datesList:
            rateKey = self.findKeyFromRateTable(rateDict, element)
            
            rate = rateDict[rateKey]
            pair = (element, rate)
            
            listWithRates.append(pair)
            
        return listWithRates
        

            
            
rateDictionary = {}
handler = apiRequestBuilder()
requestHandler = httpRequestHandler()
currency = "usd"
            


requestText = handler.buildRequest(currency, date(2022, 12, 26), date(2023, 3, 31))
rateDictionary.update(requestHandler.getCurrencyRatesInDics(requestText))



requestText = handler.buildRequest(currency, date(2023, 4, 1), date(2023, 6, 30))
rateDictionary.update(requestHandler.getCurrencyRatesInDics(requestText))



requestText = handler.buildRequest(currency, date(2023, 7, 1), date(2023, 9, 30))
rateDictionary.update(requestHandler.getCurrencyRatesInDics(requestText))



requestText = handler.buildRequest(currency, date(2023, 10, 1), date(2023, 12, 31))
rateDictionary.update(requestHandler.getCurrencyRatesInDics(requestText))



fileName = 'oneColumnShortTest.csv'
csvHandler = getDataFromOneColumnCSV()
datesList = csvHandler.getDatesListFromFile(fileName)
calculator = mainCalculator()
resultList = calculator.mapRateToDate(rateDictionary, datesList)
        


print(resultList)

csvWriter = csvWriterClass()

csvWriter.writeToFile("result1.csv", resultList)





class TestingClass(unittest.TestCase):
  

    
    def test_dataRateSchift1(self):
        calculator = mainCalculator()
        rateDict  = {"2021-10-01": 2, "2021-10-02": 3}
        self.assertEqual(calculator.findKeyFromRateTable(rateDict,"2021-10-03"), "2021-10-02")
        
    def test_dataRateSchift2(self):
        calculator = mainCalculator()
        rateDict  = {"2020-12-31": 2, "2021-10-01": 2, "2021-10-02": 3}
        self.assertEqual(calculator.findKeyFromRateTable(rateDict,"2021-01-01"), "2020-12-31")
        

        
    def test_e2e1(self):
        handler = apiRequestBuilder()
        requestText = handler.buildRequest("eur", date(2023, 2, 1), date(2023, 3, 31))
        requestHandler = httpRequestHandler()
        rateDictionary = requestHandler.getCurrencyRatesInDics(requestText)
        fileName = 'oneColumnShortTest.csv'
        csvHandler = getDataFromOneColumnCSV()
        datesList = csvHandler.getDatesListFromFile(fileName)
        calculator = mainCalculator()
        resultList = calculator.mapRateToDate(rateDictionary, datesList)
        self.assertEqual(len(resultList), 4)
        
        


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)