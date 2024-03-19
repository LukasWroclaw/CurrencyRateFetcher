#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:25:56 2024

@author: ola
"""

import csv
import unittest

testuj = 0


class csvWriterClass(object):
    
    def writeToFile(self, fileName, listWithContent):
    
    
        with open(fileName, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            for element in listWithContent:
                spamwriter.writerow(element)
                
