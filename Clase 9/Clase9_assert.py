# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:26:29 2023

@author: User
"""

import math
x = float(input('Enter a number: '))
assert x >= 0.0, 'No puede ser un numero negativo'
x = math.sqrt(x)
print(x)



def dividir(a, b):
    assert b != 0, "El denominador no puede ser cero."
    return a / b

resultado = dividir(10, 2)  # Esto funcionará bien.
print(resultado)

resultado = dividir(10, 0)  # Esto generará un AssertionError con el mensaje especificado.
print(resultado)