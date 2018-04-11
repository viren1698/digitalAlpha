# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:22:56 2018

@author: user
"""

import string
import random

length = random.randint(7, 14)

set1 = string.ascii_uppercase                   
set2 = string.digits                           
set3 = string.digits + string.ascii_letters    
build = [set1, set2] + [set3] * (length - 2)   
random.shuffle(build)                        

password = []
index = 0
last = ''

while len(password) < length:              
    choice = random.choice(build[index])
    if choice != last:
        password.append(choice)
        index += 1
        last = choice

print (password)
