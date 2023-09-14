# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:54:41 2023

@author: User
"""
##La funcion puede tener valores de retorno
def resta(a,b):
    print(a-b)
    return a-b
    print("Con el return sale de la función")

x = resta(5,1)
print("La resta es", x)
opt = x + 1
print(opt)


## Prueba  (no le hizo caso)
y = 0
def resta(a,b):
    y = a-b  # es que es variable local
    #print(a-b)
    

z = resta(10,25)
print(y)


## HAY QUE RETORNAR EL VALOR, si no no le hace caso parece
def resta(a,b):
    y = a-b
    return y
    
print(resta(10,25))
