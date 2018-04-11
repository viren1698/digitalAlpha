# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:10:34 2018

@author: user
"""

n=int(input("enter value of n"))
for i in range(n):
    print(i)

print("numbers divisible by %d are"%n)
for i in range(500):
    if(i%n==0):
        print(i)
print("value of n + nn + nnn is")
print(n + n**2 + n**3)       

print("pascal triangle")
def printPascal(n) :
     

    for line in range(0, n) :
         
       
        for i in range(0, line + 1) :
            print(binomialCoeff(line, i),
                  " ", end = "")
        print()
     
 
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
    return res
 

printPascal(n) 

print("sum of series, 1 + ½ + 1/3 +……. + 1/n is \n")
sum=0
for i in range(1,n+1):
    sum+=1/i
    
print(sum)
    
