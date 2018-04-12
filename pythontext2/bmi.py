# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:00:29 2018

@author: user
"""

import pandas as pd

 
df = pd.read_excel('student.xlsx', sheet_name='Sheet1')
print("Retrieve the data from file and print it")
print(df)

#test = df.sort_values(['height'], ascending=[False])
test = df.sort_values(['height'], ascending=[0])
print("\n\n\nPrint the students in the order of their height ")
print(test)
bmi=[]
category=[]
print("\n\n\n Calculate the BMI and print it by adding an extra field BMI to the table")
for i in range(len(df['height'])):
    bmi.append(df['weight'][i]/(df['height'][i]**2))
    bm=df['weight'][i]/(df['height'][i]**2)
    if(bm>18.5 and bm<25):
        category.append("Healthy Weight")
    elif(bm>25):
         category.append("Overweight")
    else:
        category.append("Obese")
        
        

df['bmi']=bmi
df['category']=category
print(df)
#print(df.groupby(['category',"bmi"]))


print("\n\n\n Group them by BMI")
#group by category done using sort in category feild

print(df.sort_values(by='category', ascending=False))

'''output'''

# =============================================================================
# '''
# Retrieve the data from file and print it
#        name  age  gender  height  weight
# 0  virendra   22    male    1.75      75
# 1      atul   23    male    1.80      72
# 2     rahul   25  female    1.81      75
# 3    prabal   30    male    1.65      80
# 4    kartik   82  female    1.45     110
# 5     rajan   23    male    2.80      72
# 
# 
# 
# Print the students in the order of their height 
#        name  age  gender  height  weight
# 5     rajan   23    male    2.80      72
# 2     rahul   25  female    1.81      75
# 1      atul   23    male    1.80      72
# 0  virendra   22    male    1.75      75
# 3    prabal   30    male    1.65      80
# 4    kartik   82  female    1.45     110
# 
# 
# 
#  Calculate the BMI and print it by adding an extra field BMI to the table
#        name  age  gender  height  weight        bmi        category
# 0  virendra   22    male    1.75      75  24.489796  Healthy Weight
# 1      atul   23    male    1.80      72  22.222222  Healthy Weight
# 2     rahul   25  female    1.81      75  22.893074  Healthy Weight
# 3    prabal   30    male    1.65      80  29.384757      Overweight
# 4    kartik   82  female    1.45     110  52.318668      Overweight
# 5     rajan   23    male    2.80      72   9.183673           Obese
# 
# 
# 
#  Group them by BMI
#        name  age  gender  height  weight        bmi        category
# 3    prabal   30    male    1.65      80  29.384757      Overweight
# 4    kartik   82  female    1.45     110  52.318668      Overweight
# 5     rajan   23    male    2.80      72   9.183673           Obese
# 0  virendra   22    male    1.75      75  24.489796  Healthy Weight
# 1      atul   23    male    1.80      72  22.222222  Healthy Weight
# 2     rahul   25  female    1.81      75  22.893074  Healthy Weight
# '''
# =============================================================================



