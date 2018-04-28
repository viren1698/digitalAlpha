# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:19:54 2018

@author: user
"""

import math

def sigmoid(x):
    return(1/(1+math.exp(-x)))
    
    

input_matrix=[0.05,0.10]
weight_matrix = [[0.15,0.25],[0.2,0.3]]
weight_matrix2 = [[0.40,0.50],[0.45,0.55]]
target=[.01,0.99]
b=[.35,.60]
h=[]
hout=[]
o=[]
oout=[]

for i in range(len(input_matrix)):
    sum=0
    for j in range (len(input_matrix)):
        sum+=input_matrix[j]*weight_matrix[j][i]
#        print(str((input_matrix[j]))+"*"+str(weight_matrix[j][i]))
    h.append(sum+b[0])
    hout.append(sigmoid(sum+b[0]))
    
    sum2=0
    for k in range(len(input_matrix)):
        sum2+=(sum+b[0])*weight_matrix2[k][i]
#        print(str((sum+b[0]))+"*"+str(weight_matrix2[k][i]))
    o.append(sum2+b[1])
    oout.append(sigmoid(sum2+b[1]))

print(h)
print(hout)
print(o)
print(oout)


    

    
        
