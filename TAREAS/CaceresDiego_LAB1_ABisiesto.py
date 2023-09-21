# -*- coding: utf-8 -*-
"""
        TAREA Python Essentials
        
Nombre: Diego Cáceres

        LABORATORIO 1
        
"""


"""
Todos los años bisiestos son divisibles entre 4.
Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos.
Los años que son divisibles entre 100, pero no entre 400, no son bisiestos.
Sin embargo, los años divisibles entre 100 y entre 400 sí que son bisiestos.

Fuente: https://www.smartick.es/blog/padres-y-profesores/educacion/matematicas-bisiesto/#:~:text=Todos%20los%20a%C3%B1os%20bisiestos%20son,400%20s%C3%AD%20que%20son%20bisiestos.

"""

def isYearLeap(year):
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
        return True
    else:
        return False


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else: 
        print("Failed")
