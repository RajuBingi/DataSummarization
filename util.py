#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:27:57 2019

@author: rajubingi
"""

def getCleansingNames (names, isList ):
 
     cleansed_names = []
     cleansed_names_error = []
     row_no = 0
     #print ('function in')
     #print (names)
     if (isList == 'N' or isList == 'n' ):
        names = names.split('|')
     
     for sublist in names:
        row_no = row_no + 1
        try:
          for item in sublist.split('|'):
        
            
            item = item.split('@', 1)[0]
            item = item.split('/', 1)[0]
            item = item.split('AT', 1)[0]
            item = item.replace('- ECT', '')
            item = item.replace ('.',' ')
            cleansed_names.append(item.title())
        except:
          cleansed_names_error.append(row_no)
     
     return cleansed_names  , cleansed_names_error

def getListCount(cleansed_names):      
     list_count = []
     for name in set(cleansed_names):
        count = cleansed_names.count(name)
        list_count.append((name,count ))
     
    
     
     return list_count

def flattened (ListNames):
        flattened = []
        for sublist in ListNames:
            for val in sublist:
                flattened.append(val)
                
        return flattened