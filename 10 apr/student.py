# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:42:34 2018

@author: user
"""

student=[]
eng=[]
math=[]
sst=[]
sci=[]
total=[]

for i in range(4):
    student.append(input("enter name of student"))
    eng.append(int(input("enter marks of english")))
    math.append(int(input("enter marks of math")))
    sst.append(int(input("enter marks of sst")))
    sci.append(int(input("enter marks of sci")))
    total.append(eng[i]+math[i]+sst[i]+sci[i])
    
    
for i in range(4):
    print(max(eng[i],math[i],sst[i],sci[i]))
    
topperst=0
toppertotal=total[0]
for i in range(1,4):
    if(toppertotal<total[i]):
        toppertotal=total[i]
        topperst=i

print("topper student is %d with %d marks "%(topperst+1,toppertotal))

print("english \t maths \t sst \t sci \n")
for i in range(2):
    print("%d \t %d \t %d \t %d"%(eng[i],math[i],sst[i],sci[i]))

n = len(eng)

for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if total[j] < total[j+1] :
                total[j], total[j+1] = total[j+1], total[j]
                student[j], student[j+1] = student[j+1], student[j]
                eng[j], eng[j+1] = eng[j+1], eng[j]
                math[j], math[j+1] = math[j+1], math[j]
                sst[j], sst[j+1] = sst[j+1], sst[j]
                sci[j], sci[j+1] = sci[j+1], sci[j]
                
     
for i in range(4):
    print("%s %d \t %d \t %d \t %d \t %d"%(student[i],eng[i],math[i],sst[i],sci[i],total[i]))    


print("student list sorted in respected to total marks")

for i in range(2):
    student.append(input("enter name of student"))
    eng.append(int(input("enter marks of english")))
    math.append(int(input("enter marks of math")))
    sst.append(int(input("enter marks of sst")))
    sci.append(int(input("enter marks of sci")))
    total.append(eng[4+i]+math[4+i]+sst[4+i]+sci[4+i])    


print("updated list with 4th and fidth student")
for i in range(4):
    print("%s %d \t %d \t %d \t %d \t %d"%(student[i],eng[i],math[i],sst[i],sci[i],total[i]))    

    



    

    
