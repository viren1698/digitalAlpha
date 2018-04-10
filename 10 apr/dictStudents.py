# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:18:21 2018

@author: user
"""
import pandas as pd

result={"name":["viredra","atuk","sid","khan","akram","shahid"],"score":[33,23,45,34,45,55],"no_of_attempts":[1,3,4,4,4,4],"qualify":["yes","no","no","no","no","yes"]}
name=result.get("name")
scare=result.get("score")
attempts=result.get("no_of_attempts")
qualify=result.get("qualify")
labels={"labels":["a","b","c","d","e","f"]}
df=pd.DataFrame(result,index=labels["labels"])
print(df)

print(df.head(4))

print(pd.DataFrame(qualify,index=df["name"]))

totalattpt=0
for i in range(len(df["name"])):
    if(df["score"][i]>20 and df["score"][i]<35):
        print("%s score= %d \t no of attempts= %d "% (df["name"][i],df["score"][i],df["no_of_attempts"][i]))
        totalattpt+=df["no_of_attempts"][i]
print("total attempts by these students %d"%totalattpt)



