# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:30:25 2023

@author: User
"""
'''
import math

x = float(input("Enter x: "))
y = math.sqrt(x)  #Errores, podria poner algo que no sea un numero o un numero negativo


value = 1
value /= 0


list = []
x = list[0]  ##Asignamos algo vacio, (buscamos un puntero que no existe)
'''
print("INICIO")
try:
    print("1")
    x = 1/0
    print("2")
except:
    print("Hay un error")

print("3")
print("FIN")
        