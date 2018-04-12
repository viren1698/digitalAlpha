# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:35:54 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt 
 
df = pd.read_csv('camera.csv')
print("Print the properties of the data set\n")
print(df.columns)
print("\n\n\n\nPrint the data types of properties group wise\n")
g = df.columns.to_series().groupby(df.dtypes).groups
print(g)
print("\n\n\n\nPrint the data types of properties individual column wise\n")
print(df.dtypes)

print("\n \n \n Print the model, release date and price of first 25 entries")
df1 =  df[['Model','Release date', 'Price']][:25]
print(df1)

print("\n\n\nprice statistics\n")
print(pd.to_numeric(df["Price"]).describe())

print("time series graph price>1000")
plt.plot(pd.to_numeric(df["Release date"]),pd.to_numeric(df["Price"])>1000,color='red')
plt.show()

pd.crosstab(pd.to_numeric(df["Release date"]),pd.to_numeric(df["Price"])>1000).plot(kind='bar')
plt.title('Release date vs Price')
plt.xlabel('Release date')
plt.ylabel('Price')
plt.savefig('Release datevsprice') 

pd.crosstab(df["Effective pixels"],df["Price"]).plot(kind='bar')
plt.title('Effective pixels vs Price')
plt.xlabel('Effective pixels')
plt.ylabel('Price')
plt.savefig('Effective pixelsvsprice') 



pd.crosstab(df["Model"],df["Price"]).plot(kind='bar')
plt.title('Model vs Price')
plt.xlabel('Model')
plt.ylabel('Price')
plt.savefig('Modelvsprice') 



pd.crosstab(df["Price"],df["Release date"]).plot(kind='bar')
plt.title('Price vs R date')
plt.xlabel('Price')
plt.ylabel('R date')
plt.savefig('pricevsRdate') 


pd.crosstab(df["Weight (inc. batteries)"],df["Price"]).plot(kind='bar')
plt.title('Weight vs Price')
plt.xlabel('Weight')
plt.ylabel('Price')
plt.savefig('wt vs Price')  

pd.crosstab(df["Price"],df["Storage included"]).plot(kind='bar')
plt.title('Price vs Storage')
plt.xlabel('Price')
plt.ylabel('Storage')
plt.savefig('PricevsStorage')  







