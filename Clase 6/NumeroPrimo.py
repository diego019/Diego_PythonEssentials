# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:49:15 2023

@author: User
"""

def EsPrimo(num):
    c = 0
    for i in range(1,num+1,1):
        print(num%i)
        if num % i == 0:
            c += 1
    if c>2:
        return False
    else:
        return True
        
z = EsPrimo(29)

if  z == True:
    print("Es primo")
else:
    print("No es primo")   
    
"""
for i in range(1,20):
    if EsPrimo(i+1):
        print(i+1, end ="")
"""