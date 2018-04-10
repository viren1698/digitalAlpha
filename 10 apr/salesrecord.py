import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import numpy
 
df = pd.read_csv(r'100 Sales Records.csv')
print(df.head)

print(df.columns)

print(df[:10])
plt.plot(df.index,df["Total Profit"])
plt.show()

itemtype=df["Item Type"]
totalcost=df["Total Cost"]
set11=set()

for i in range(len(itemtype)):
    if(totalcost[i]>1000000):
        set11.add(itemtype[i])
        #print("%s = %d " % (itemtype[i],totalcost[i]))
print(set11)        
