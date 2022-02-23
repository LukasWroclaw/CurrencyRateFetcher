# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:16:22 2022



@author: marszale
"""


import csv
import unittest

testuj = 0

class getDataFromCSVhandlerMintos(object):
    
    def isIncome(self, detailsString):
        if "interest received" in detailsString:
            return 1
        elif "late fees received" in detailsString:
            return 1
        
        return 0
    
    def convertDate(self, rawDate):
        splitted = rawDate.split(".")
        
        dayInt = int(splitted[0])
        
        if dayInt < 10:
            day = "0" + str(dayInt)
        else:
            day = str(dayInt)
            
            
        monthInt = int(splitted[1])
        
        if monthInt < 10:
            month = "0" + str(monthInt)
        else:
            month = str(monthInt)
        
        
        trimmedYear = str((splitted[2])[:4])
        
        return trimmedYear + "-"  + month + "-" + day
    
    def getDataFromFile(self, fileName):
        with open(fileName, mode='r') as csv_file:
            incr = 0;
            listOfRows = []
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                listOfRows.append(row)
                incr+=1
                
            return listOfRows

    def addOrUpdateElementInDictionary(self, dictionary, key, value):
        if key in dictionary:
             dictionary[key] = dictionary[key] + value
        else:
             dictionary[key] = value
    
    def getConvertedData(self, listOfRows):
        dictionaryWithIncome = {}
        
       
        for row in listOfRows:           
           if self.isIncome(row["Details"]):
               key = self.convertDate(row["Date"])
               self.addOrUpdateElementInDictionary(dictionaryWithIncome, key, float(row["Turnover"]))
              
          
        return dictionaryWithIncome
    
    
    def getIncomeDictionaryFromFile(self, fileName):
        listWithData = self.getDataFromFile(fileName)
        incomeDictionary = self.getConvertedData(listWithData)
        
        return incomeDictionary
        
        
    
        
        
class TestingClass(unittest.TestCase):
    
    def test_e2eFunction(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            incomeDictionary = handler.getIncomeDictionaryFromFile(fileName)
            incomeForParticularDay = incomeDictionary['2022-01-01']
            self.assertEqual(incomeForParticularDay, 0.082874284)
  
    def test_getConvertedData1(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            incomeDictionary = handler.getConvertedData(listWithData)
            incomeForParticularDay = incomeDictionary['2022-01-01']
            self.assertEqual(incomeForParticularDay, 0.082874284)



    def test_getConvertedData2(self):
            fileName = 'tableForTest.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            incomeDictionary = handler.getConvertedData(listWithData)
            incomeForParticularDay = incomeDictionary['2022-01-07']
            self.assertEqual(incomeForParticularDay, 0.113679132)
  
    
    def test_getDataFromFile1(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            self.assertEqual(len(listWithData), 5)
            
    def test_getDataFromFile2(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            secondRow = listWithData[1]
            self.assertEqual(secondRow['Transaction ID:'], '2')
    
    def test_isIncome1(self):
            detailsText = "Loan 4 - investment in loan "
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 0)
            
    def test_isIncome2(self):
            detailsText = "Loan 1 - The loan was repurchased. Reason: The loan agreement was amended.: interest received "
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 1)
            

    def test_isIncome3(self):
            detailsText = "Loan 5 - late fees received"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 1)
            
            
    def test_dateConversion1(self):
            rawDateText = "10.01.2022  12:11:00"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.convertDate(rawDateText), "2022-01-10")


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)  