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
        incomeStrings = ["Interest received", "Late fees received", "Interest received from loan repurchase", "Interest received from overdue payments"]
        
        for element in incomeStrings:
            if element in detailsString:
                return 1
        
        
        return 0
    
    def isTax(self, detailsString):
        
        if detailsString in "Tax withholding" :
            return 1
        
        return 0
        
    
    def convertDate(self, rawDate):
        dateAndHour = rawDate.split(" ")
        dateOnly = dateAndHour[0]
        splitted = dateOnly.split("-")
        
        year = splitted[0]
        

        monthInt = int(splitted[1])
        
        if monthInt < 10:
            month = "0" + str(monthInt)
        else:
            month = str(monthInt)
            
        dayInt = int(splitted[2])
        
        if dayInt < 10:
            day = "0" + str(dayInt)
        else:
            day = str(dayInt)      
        
        

        
        return year + "-"  + month + "-" + day
    
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
        dictionaryWithTax = {}
        
       
        for row in listOfRows:           
           if self.isIncome(row["Payment Type"]):
               key = self.convertDate(row["Date"])
               self.addOrUpdateElementInDictionary(dictionaryWithIncome, key, float(row["Turnover"]))
               
           elif self.isTax(row["Payment Type"]):
               key = self.convertDate(row["Date"])
               self.addOrUpdateElementInDictionary(dictionaryWithTax, key, float(row["Turnover"]))
              
          
        return dictionaryWithIncome, dictionaryWithTax
    
    
    def getIncomeAndTaxDictionaryFromFile(self, fileName):
        listWithData = self.getDataFromFile(fileName)
        incomeDictionary, dictionaryWithTax = self.getConvertedData(listWithData)
        
        return incomeDictionary, dictionaryWithTax
        
        
    
        
        
class TestingClass(unittest.TestCase):
    
    def test_e2eFunction(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            incomeDictionary, taxDictrionary = handler.getIncomeAndTaxDictionaryFromFile(fileName)
            incomeForParticularDay = incomeDictionary['2023-04-04']
            taxForParticularDay = taxDictrionary['2023-04-05']
            self.assertEqual(incomeForParticularDay, 0.38)
            self.assertEqual(taxForParticularDay, -0.05)
  
    def test_getConvertedData1(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            incomeDictionary, taxDictrionary = handler.getConvertedData(listWithData)
            incomeForParticularDay = incomeDictionary['2023-04-04']
            self.assertEqual(incomeForParticularDay, 0.38)


  
    
    def test_getDataFromFile1(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            self.assertEqual(len(listWithData), 6)
            
    def test_getDataFromFile2(self):
            fileName = 'tableForTestShort.csv'
            handler = getDataFromCSVhandlerMintos()
            listWithData = handler.getDataFromFile(fileName)
            secondRow = listWithData[1]
            self.assertEqual(secondRow['Transaction ID:'], '2')
    
    def test_isIncome1(self):
            detailsText = "Interest received"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 1)
            
    def test_isIncome2(self):
            detailsText = "Interest received from loan repurchase"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 1)
            

    def test_isIncome3(self):
            detailsText = "Late fees received"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 1)
            
    def test_isIncome4(self):
            detailsText = "Tax withholding"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isIncome(detailsText), 0)
            
    def test_isTax1(self):
            detailsText = "Tax withholding"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isTax(detailsText), 1)
            
    def test_isTax2(self):
            detailsText = "Late fees received"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.isTax(detailsText), 0)
            
            
    def test_dateConversion1(self):
            rawDateText = "2023-01-02 11:26:04"
            handler = getDataFromCSVhandlerMintos()
            self.assertEqual(handler.convertDate(rawDateText), "2023-01-02")


if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)  