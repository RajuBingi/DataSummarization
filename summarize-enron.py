#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:32:26 2019

@author: rajubingi
"""


import sys
from BNPP import BNPP1, BNPP2


csv_status = BNPP1(sys.argv[1])

if csv_status == 0:
  visual_status =  BNPP2(sys.argv[1]) 
  
  
else:
  print("CSV file can not be generated" )


