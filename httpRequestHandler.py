# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:31:10 2022

@author: marszale
"""

import unittest

import requests
testuj = 1
    
class httpRequestHandler(object):
    
    def getJsonFileFromUrl(self, urlAddress):
        try:
            response = requests.get(urlAddress)
        except:
            print("Page not opened! ", urlAddress)
            return ""
            
        return response.json()
    
    def convertJsonToDict(self, jsonInput):
        dictForRates = {}
        
        rates = jsonInput["rates"]
        
        for element in rates:
            date = str(element['effectiveDate'])
            value = float(element['mid'])
            dictForRates[date] = value
            
        return dictForRates
            
        


class TestingClass(unittest.TestCase):
  
    
    def test_basic1(self):
            requestText = "http://api.nbp.pl/api/exchangerates/rates/a/eur/2021-01-04/2021-01-07/"
            requestHandler = httpRequestHandler()
            receivedJson = requestHandler.getJsonFileFromUrl(requestText)
            dictionary = requestHandler.convertJsonToDict(receivedJson)
            expectedDict = {'2021-01-04': 4.5485, '2021-01-05': 4.5446, '2021-01-07': 4.4973}
            self.assertEqual(dictionary, expectedDict)



if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)      