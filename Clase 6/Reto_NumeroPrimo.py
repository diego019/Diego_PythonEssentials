# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:49:15 2023

@author: User
"""

def EsPrimo(num):
    c = 0
    #print(num)
    if num > 1:
        for i in range(1,num+1,1):
            #print(num%i)
            if num % i == 0:
                c += 1
        if c>2:
            return False
        else:
            return True
    else:
        return 10
        

numero = 10
z = EsPrimo(numero)
if  z == True:
    print("El numero", numero, " es primo \n")
elif z == False:
    print("El numero", numero, " no es primo \n")   
elif z == 10:
  print("Un número primo es un número natural, mayor que 1, que tiene sólo, dos divisores.")
  
#Un número primo es un número natural, mayor que 1, que tiene sólo, dos divisores.
 
for i in range(1, 100):
    if EsPrimo (i + 1):
        print(i + 1, end=" ")