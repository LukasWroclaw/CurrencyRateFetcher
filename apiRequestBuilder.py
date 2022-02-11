# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:36:20 2022

@author: marszale

"""
from datetime import date
import unittest
testuj = 0

## http://api.nbp.pl/api/exchangerates/rates/a/gbp/2012-01-01/2012-01-31/

class apiRequestBuilder(object):
    prefixText = "http://api.nbp.pl/api/exchangerates/rates/a/"
    
    
    def intToStrWithZero(self, inputNumber):
        number = int(inputNumber)
        
        if number < 10:
            return "0" + str(number)
        else:
            return str(number)
        
    
    def convertDateToRequestFormat(self, date):
        year = str(date.year)
        month = self.intToStrWithZero(date.month)
        day = self.intToStrWithZero(date.day)
            
        
        
        return year + "-" + month + "-" + day
    
    def buildRequest(self, currency="eur", startDate=date(2021, 1, 1), endDate=date(2021, 1, 31)):
        requestText = self.prefixText + currency + "/" + self.convertDateToRequestFormat(startDate) + "/" + self.convertDateToRequestFormat(endDate) + "/"
        return requestText;
    
    
        
    
    


class TestingClass(unittest.TestCase):
  
    
    def test_dateConverstion1(self):
        handler = apiRequestBuilder()
        requestText = handler.convertDateToRequestFormat(date(2021, 10, 30))
        self.assertEqual(requestText, "2021-10-30")
 
    def test_dateConverstion2(self):
        handler = apiRequestBuilder()
        requestText = handler.convertDateToRequestFormat(date(2021, 1, 1))
        self.assertEqual(requestText, "2021-01-01")       

    
    def test_basic1(self):
        handler = apiRequestBuilder()
        requestText = handler.buildRequest()
        self.assertEqual(requestText, "http://api.nbp.pl/api/exchangerates/rates/a/eur/2021-01-01/2021-01-31/")
        
    def test_basic2(self):
        handler = apiRequestBuilder()
        requestText = handler.buildRequest("usd", date(2022, 2, 2), date(2022, 2, 4))
        self.assertEqual(requestText, "http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-02-02/2022-02-04/")
    


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)