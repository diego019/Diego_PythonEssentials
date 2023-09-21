# -*- coding: utf-8 -*-
"""
        TAREA Python Essentials
        
Nombre: Diego Cáceres

        LABORATORIO 2
        
"""

def isYearLeap(year):
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
        return True
    else:
        return False

'''
Enero: 31 días
Febrero: 28 o 29 días (si es año bisiesto)
Marzo: 31 días
Abril: 30 días
Mayo: 31 días 
Junio: 30 días 
Julio: 31 días
Agosto: 31 días
Septiembre: 30 días
Octubre: 31 días
Noviembre: 30 días
Diciembre: 31 días
'''

def daysInMonth(year, month):
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        if month > 12 or month < 1 or year < 1:   ##Que sea valido desde el año 1 (opcional)  #NOTA: el mes no es necesario (el codigo siguiente si devolveria None)
            return None
        for i in range(len(dias)+1):
            if(month == i):
                if (isYearLeap(year) and month == 2):
                    return dias[i-1]+1   ##29 dias para febrero
                return dias[i-1] 
    except Exception:
        return None
    

 

testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result != None:
        if result == testResults[i]:
            print("OK")
        else:
            print("Failed")
    else:
        print(None)