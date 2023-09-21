# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 08:46:45 2023

@author: Juan Carlos
"""

class DivisionPorCeroError(Exception):
    pass

class Calculadora:
    def dividir(self, num1, num2):
        if num2 == 0:
            raise DivisionPorCeroError("División por cero no permitida")
        return num1 / num2

try:
    calc = Calculadora()
    resultado = calc.dividir(10, 0)
    print("El resultado es:", resultado)
except DivisionPorCeroError as e:
    print("Error:", e)
