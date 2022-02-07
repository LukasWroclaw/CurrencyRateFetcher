# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:31:10 2022

@author: marszale
"""

import requests

    
class httpRequestHandler(object):
    
    def getJsonFileFromUrl(self, urlAddress):
        try:
            response = requests.get(urlAddress)
        except:
            print("Page not opened! ", urlAddress)
            return ""
            
        return response.json()

