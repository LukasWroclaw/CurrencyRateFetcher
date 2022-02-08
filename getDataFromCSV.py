# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:16:22 2022

@author: marszale
"""

from datetime import date
import csv
import unittest

testuj = 1

class getDataFromCSVhandler(object):
    
    def isIncome(self, detailsString):
        if "interest received" in detailsString:
            return 1
        elif "late fees received" in detailsString:
            return 1
        
        return 0
    
    def convertDate(self, rawDate):
      
        splitted = rawDate.split(".")
        day = int(splitted[0])
        month = int(splitted[1])
        trimmedYear = int((splitted[2])[:4])
        
        return date(trimmedYear,month,day)
        
        
"""
"10.01.2022  12:11:00"

with open('tableForTest.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        print(row)
        
"""        
        
        
class TestingClass(unittest.TestCase):
  
    
    def test_isIncome1(self):
            detailsText = "Loan 4 - investment in loan "
            handler = getDataFromCSVhandler()
            self.assertEqual(handler.isIncome(detailsText), 0)
            
    def test_isIncome2(self):
            detailsText = "Loan 1 - The loan was repurchased. Reason: The loan agreement was amended.: interest received "
            handler = getDataFromCSVhandler()
            self.assertEqual(handler.isIncome(detailsText), 1)
            

    def test_isIncome3(self):
            detailsText = "Loan 5 - late fees received"
            handler = getDataFromCSVhandler()
            self.assertEqual(handler.isIncome(detailsText), 1)
            
            
    def test_dateConversion1(self):
            rawDateText = "10.01.2022  12:11:00"
            handler = getDataFromCSVhandler()
            self.assertEqual(handler.convertDate(rawDateText), date(2022, 1, 10))


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)  