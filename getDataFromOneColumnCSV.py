# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:16:22 2022



@author: marszale
"""


import csv
import unittest

testuj = 0

class getDataFromOneColumnCSV(object):
    

    
    def getDataFromFile(self, fileName):
        with open(fileName, mode='r') as csv_file:
            incr = 0;
            listOfRows = []
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                listOfRows.append(row)
                incr+=1
                
            return listOfRows


    
    def getConvertedData(self, listOfRows):
        datesList = []
        
       
        for row in listOfRows:           
            datesList.append(row["Date"])

              
          
        return datesList
    
    
    def getDatesListFromFile(self, fileName):
        listWithData = self.getDataFromFile(fileName)
        datesList = self.getConvertedData(listWithData)
        
        return datesList
        
        
    
        
        
class TestingClass(unittest.TestCase):
    
    def test_e2eFunction(self):
            fileName = 'oneColumnShortTest.csv'
            handler = getDataFromOneColumnCSV()
            datesList = handler.getDatesListFromFile(fileName)
            numberOfElements = len(datesList)
            self.assertEqual(numberOfElements, 4) 




if(testuj):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)  