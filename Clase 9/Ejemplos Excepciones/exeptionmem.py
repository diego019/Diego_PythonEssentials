# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:54:24 2020

@author: Juan Carlos
"""

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')
    
    
    
'''
MemoryError es una excepción que se genera en Python cuando el programa se queda sin memoria disponible en la memoria RAM del sistema. Esto significa que el programa intentó asignar más memoria de la que el sistema operativo podía proporcionar, lo que generalmente ocurre cuando se está trabajando con grandes conjuntos de datos o se está utilizando una cantidad excesiva de memoria en un programa.
'''


#ejemplo: 
# Generar un MemoryError de forma deliberada al crear una lista grande.
try:
    lista_grande = [0] * (10 ** 8)  # Esto intentará crear una lista con 100 millones de elementos.
except MemoryError:
    print("Se ha producido un MemoryError. El programa se quedó sin memoria.")