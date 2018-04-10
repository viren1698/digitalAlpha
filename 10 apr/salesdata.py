# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:50:44 2018

@author: user
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import numpy
 
df = pd.read_excel(r'salestable.xlsx')
print(df.head)
extprice=[]
extprice=df["Ext price"]

print(df.columns)
print(df.describe())
print(df.dtypes)

print(df[:10])
print(df[['Name','Ext price']])
