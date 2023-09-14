# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:02:22 2023

@author: User
"""

nombre = input("Ingrese el nombre: ")
#Cada vez que utilice el input siempre va a ser una cadena de caracteres o string
print(nombre)

'''
numero = int(input("Ingrese un número: "))
print(numero)
'''


#Lo que dice:
    
while True:
    try:
        numero = int(input("Ingrese un número: "))
        print(numero)
        break  # Sale del bucle si se ingresa un número válido
    except ValueError:
        print("Eso no es un número válido. Intente nuevamente.")