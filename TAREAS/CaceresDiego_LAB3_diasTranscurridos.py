# -*- coding: utf-8 -*-
"""
        TAREA Python Essentials
        
Nombre: Diego Cáceres

        LABORATORIO 3
        
"""
#En clase se aclaró que la funcion recibe la fecha (dia, mes, año) 
#y debe devolver cuantos dias han transcurrido desde el inicio del año


#NOTA: Consideré desde el inicio del año hasta la fecha que recibe la funcion (considerado como dia transcurrido)
#Si no se desea considerar como dia trancurrido la fecha que recibe solo seria de restar 1

def isYearLeap(year):
    if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
        return True
    else:
        return False
 

def daysInMonth(year, month):
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(dias)+1):
        if(month == i):
            if (isYearLeap(year) and month == 2):
                return dias[i-1]+1   ##29 dias para febrero
            return dias[i-1] 
 
 

def dayOfYear(year, month, day):
   try:
       if year < 1 or month > 12 or month < 1:   ##considerando desde el año 1
           return None
       if day > daysInMonth(year,month):  
           return None
       diasT = 0
       for i in range(1, month, 1):
           diasT += daysInMonth(year,i)
       diasT += day
       print('Días transcurridos desde el inicio del año '+ str(year) + " hasta " 
             +str(year)+"/"+str(month)+"/"+str(day), end =' : ')
       return diasT
   except Exception:
       return None
   
print(dayOfYear(2000, 12, 31))  ## el año 2000 tuvo 366 dias  (año bisiesto)

print(dayOfYear(2021, 12, 31))  ## el año 2021 tuvo 365 dias 

print(dayOfYear(2008, 12, 31))  ## el año 2008 tuvo 366 dias  (año bisiesto)

print(dayOfYear(2023, 9, 19))   ## desde que inicio este año hasta la fecha que entregue el deber 262 dias 

print(dayOfYear(2021, 1,5 ))   ## 5 de enero (5 dias) 

print(dayOfYear(2023, 5, 10))   ## 10 de mayo (130 dias)

print(dayOfYear(2023, 13, 10))   ## Mes 13 no existe, devuelve None

print(dayOfYear(2023, 13, 'a'))   ## Argumento de dia invalido, devuelve None